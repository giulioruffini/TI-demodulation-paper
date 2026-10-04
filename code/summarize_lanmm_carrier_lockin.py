"""Summarize the R6 lock-in caches without rerunning the LaNMM simulation.

S(fc) is the arithmetic mean of |I+iQ| over beats in [7, 14] Hz more
than 1.5 Hz from the field-free dominant alpha frequency. Each carrier
curve is normalized by its own maximum. Field-free amplitudes are called
background, since they include autonomous spectral components as well as
finite-window leakage. Their ratios are diagnostics, not error bounds.

The frequency-dominance screen |f_out - beat| < 0.3 Hz does not establish
phase locking. A retrospective statistic numerically close to 25% does
not establish the historical provenance of the manuscript's old claim.

Usage:
    python summarize_lanmm_carrier_lockin.py --format markdown
    python summarize_lanmm_carrier_lockin.py --output /tmp/r6_summary.json
"""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def load_cache(path):
    with np.load(path, allow_pickle=False) as cache:
        return {key: cache[key] for key in cache.files}


def summarize_cache(path):
    z = load_cache(path)
    fc, beat = z["fc"], z["df"]
    selected = ((beat >= 7) & (beat <= 14)
                & (np.abs(beat - float(z["f_alpha_base"])) > 1.5))
    response = z["L1"][:, selected]
    background = z["L1_base"][selected]
    mean = response.mean(axis=1)
    normalized = mean / mean.max()
    high = (fc >= 30) & (fc <= 80)
    dominance = np.abs(z["F1c"] - beat[None, :]) < 0.3
    ridge_indices = z["L1"].argmax(axis=1)
    background_ratio = background[None, :] / response
    imax, jmax = np.unravel_index(background_ratio.argmax(), response.shape)
    at10 = int(np.flatnonzero(beat == 10)[0])
    column10 = z["L1"][:, at10]
    maximum10 = int(column10.argmax())

    record = {
        "source": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "target": str(z["target"]),
        "window_s": float(z["t_meas"]),
        "settling_s": float(z["t_settle"]),
        "dt_s": float(z["dt"]),
        "component_amplitude_mV": float(z["eps_c"]),
        "field_free_dominant_alpha_Hz": float(z["f_alpha_base"]),
        "selected_beats_Hz": beat[selected].tolist(),
        "mean_lockin_min_mV": float(mean.min()),
        "mean_lockin_max_mV": float(mean.max()),
        "peak_carrier_Hz": float(fc[mean.argmax()]),
        "normalized_30_80_Hz": {
            "min": float(normalized[high].min()),
            "max": float(normalized[high].max()),
            "median": float(np.median(normalized[high])),
        },
        "normalized_at_carrier_Hz": {
            str(carrier): float(normalized[fc == carrier][0])
            for carrier in (25, 60, 80)
        },
        "background": {
            "mean_mV": float(background.mean()),
            "max_mV": float(background.max()),
            "max_at_beat_Hz": float(beat[selected][background.argmax()]),
            "mean_over_smallest_mean_response": float(background.mean() / mean.min()),
            "max_pointwise_background_over_response": float(background_ratio.max()),
            "max_ratio_at_carrier_Hz": float(fc[imax]),
            "max_ratio_at_beat_Hz": float(beat[selected][jmax]),
            "points_response_at_or_below_background": int((response <= background).sum()),
            "amplitude_per_selected_beat_mV": background.tolist(),
        },
        "dominance_screen": {
            "tolerance_Hz": 0.3,
            "selected_points_passing": int(dominance[:, selected].sum()),
            "selected_points_total": int(response.size),
            "ridge_fraction_passing": float(
                dominance[np.arange(fc.size), ridge_indices].mean()),
            "ridge_beat_range_Hz": [float(beat[ridge_indices].min()),
                                    float(beat[ridge_indices].max())],
        },
        "retrospective_10_Hz_statistic": {
            "median_over_carriers_divided_by_max": float(np.median(column10) / column10.max()),
            "max_mV": float(column10.max()),
            "max_at_carrier_Hz": float(fc[maximum10]),
            "max_point_output_frequency_Hz": float(z["F1c"][maximum10, at10]),
            "max_point_passes_dominance_screen": bool(dominance[maximum10, at10]),
            "field_free_background_mV": float(z["L1_base"][at10]),
        },
        "per_carrier": [
            {"carrier_Hz": float(f), "mean_lockin_mV": float(s), "normalized": float(r)}
            for f, s, r in zip(fc, mean, normalized)
        ],
    }
    if record["window_s"] == 3:
        previous_path = path.parent / f"lanmm_field_{record['target']}_twotone.npz"
        previous = load_cache(previous_path)
        record["original_band_power_cache"] = {
            "source": previous_path.name,
            "relative_max_difference": {
                key: float(np.max(np.abs(z[key] - previous[key]))
                           / np.max(np.abs(previous[key])))
                for key in ("Pc1", "Pc2")
            },
        }
    return record


def summarize(input_dir):
    records = [
        summarize_cache(input_dir / f"lanmm_carrier_lockin_{target}_twotone{tag}.npz")
        for target in ("P2", "P1") for tag in ("", "_tmeas10")
    ]
    differences = {}
    for target in ("P2", "P1"):
        short, long = [record for record in records if record["target"] == target]
        if short["selected_beats_Hz"] != long["selected_beats_Hz"]:
            raise ValueError("Window comparison requires the same selected beats")
        a, b = short["per_carrier"], long["per_carrier"]
        if [row["carrier_Hz"] for row in a] != [row["carrier_Hz"] for row in b]:
            raise ValueError("Window comparison requires the same carrier grid")
        deviation = np.abs(np.array([row["normalized"] for row in a])
                           - np.array([row["normalized"] for row in b]))
        absolute = np.abs(np.array([row["mean_lockin_mV"] for row in a])
                          - np.array([row["mean_lockin_mV"] for row in b]))
        differences[target] = {
            "max_abs_normalized_difference": float(deviation.max()),
            "max_normalized_difference_at_carrier_Hz": a[int(deviation.argmax())]["carrier_Hz"],
            "max_abs_mean_lockin_difference_mV": float(absolute.max()),
        }
    return {
        "statistic": "S(fc) = arithmetic mean of lock-in amplitudes over 7–14 Hz beats more than 1.5 Hz from field-free dominant alpha; normalize by each curve's own carrier maximum",
        "interpretation": "Descriptive finite-amplitude response; unequal target amplitudes; dominance is not a phase-locking test; field-free background is not solely leakage",
        "numpy_version": np.__version__,
        "records": records,
        "window_differences": differences,
    }


def markdown(report):
    lines = [
        "S is the mean lock-in amplitude over the specified 17 beats; percentages use each carrier curve's own peak.",
        "",
        "| Drive | Window (s) | Component (mV) | S range (mV) | Peak carrier (Hz) | At 25 Hz | 30–80 Hz range (median) | At 60 / 80 Hz |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in report["records"]:
        h, at = r["normalized_30_80_Hz"], r["normalized_at_carrier_Hz"]
        lines.append(
            f"| {r['target']} | {r['window_s']:.0f} | {r['component_amplitude_mV']:.1f} "
            f"| {r['mean_lockin_min_mV']:.5f}–{r['mean_lockin_max_mV']:.5f} "
            f"| {r['peak_carrier_Hz']:.0f} | {100*at['25']:.2f}% "
            f"| {100*h['min']:.2f}–{100*h['max']:.2f}% ({100*h['median']:.2f}%) "
            f"| {100*at['60']:.2f}% / {100*at['80']:.2f}% |")
    lines += ["", "| Drive | Window (s) | Mean / max background (mV) | Mean background / minimum S | Maximum pointwise background / response |", "|---|---:|---:|---:|---:|"]
    for r in report["records"]:
        b = r["background"]
        lines.append(
            f"| {r['target']} | {r['window_s']:.0f} | {b['mean_mV']:.6f} / {b['max_mV']:.6f} "
            f"| {100*b['mean_over_smallest_mean_response']:.2f}% "
            f"| {b['max_pointwise_background_over_response']:.3f} |")
    lines += ["", "The largest background is at 8 Hz in both windows. These ratios diagnose contamination; they are not error bounds. No selected point passes the dominant-frequency screen, which does not establish phase locking.", ""]
    for target, d in report["window_differences"].items():
        lines.append(f"- {target}: maximum 3 s–10 s difference is {100*d['max_abs_normalized_difference']:.2f} percentage points at {d['max_normalized_difference_at_carrier_Hz']:.0f} Hz; maximum absolute difference is {d['max_abs_mean_lockin_difference_mV']:.5f} mV.")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=HERE)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path, help="Output file; default is standard output")
    args = parser.parse_args()
    report = summarize(args.input_dir)
    content = (json.dumps(report, indent=2, allow_nan=False) + "\n"
               if args.format == "json" else markdown(report))
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
