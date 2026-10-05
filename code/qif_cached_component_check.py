"""Measure beat and gamma components in the preserved two-tone QIF cache.

The Hann lock-in uses the stored measurement window. Gamma frequency is estimated
from the maximum in 48--58 Hz, excluding 1.5 Hz around the applied beat. This is a
spectral diagnostic, not a stability calculation or a test of phase capture.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar


def measure(t_ms, rate, beat_hz, start_index):
    t = t_ms[start_index:] / 1000.0
    x = rate[start_index:]
    mean = float(x.mean())
    w = np.hanning(len(x))
    y = (x - mean) * w

    def depth(freq):
        return float(2 * abs(np.sum(y * np.exp(-2j * np.pi * freq * t))) / w.sum() / mean)

    dt = float(np.median(np.diff(t)))
    nfft = 1 << (len(x).bit_length() + 2)
    freq = np.fft.rfftfreq(nfft, dt)
    amp = np.abs(np.fft.rfft(y, n=nfft))
    band = (freq >= 48) & (freq <= 58) & (abs(freq - beat_hz) >= 1.5)
    coarse = freq[np.flatnonzero(band)[np.argmax(amp[band])]]
    lower, upper = max(48.0, coarse - 0.2), min(58.0, coarse + 0.2)
    if coarse < beat_hz:
        upper = min(upper, beat_hz - 1.5)
    else:
        lower = max(lower, beat_hz + 1.5)
    fit = minimize_scalar(lambda f: -depth(f), bounds=(lower, upper),
                          method="bounded", options={"xatol": 1e-6})
    gamma = float(fit.x)
    bins = np.fft.rfftfreq(len(x), dt)
    bin_depths = 2 * abs(np.fft.rfft(y)) / w.sum() / mean
    bin_band = (bins >= 48) & (bins <= 58) & (abs(bins - beat_hz) >= 1.5)
    peak_bin = np.flatnonzero(bin_band)[np.argmax(bin_depths[bin_band])]
    result = dict(mean_rate_per_ms=mean, beat_Hz=float(beat_hz),
                  gamma_peak_Hz=gamma, gamma_depth=depth(gamma),
                  gamma_FFT_bin_Hz=float(bins[peak_bin]),
                  gamma_FFT_bin_depth=float(bin_depths[peak_bin]),
                  beat_depth=depth(beat_hz), sum_depth=depth(gamma + beat_hz),
                  difference_depth=depth(abs(gamma - beat_hz)),
                  window_ms=float((t[-1] - t[0] + dt) * 1000))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    path = Path(__file__).with_name("qif_raster_twotone.npz")
    cache = np.load(path, allow_pickle=True)
    meta = cache["meta"].item()
    out = {"cache_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
           "estimator": "Hann lock-in amplitude divided by the measurement-window mean",
           "conditions": {}}
    for key, condition in cache["conds"].item().items():
        q = condition["q"]
        start = q["kmeas"]
        out["conditions"][key] = {
            "qif": measure(q["ts"], q["re_t"], q["df"], start),
            "mean_field": measure(condition["mf_t"], condition["mf_re"], q["df"], start),
        }
        if key.endswith("_on"):
            rate = out["conditions"][key]["qif"]
            rate["stored_beat_depth"] = float(q["AC"] / q["rmean"])
            assert abs(rate["beat_depth"] - rate["stored_beat_depth"]) < 1e-10
    out["carrier_excursion_estimate_per_tone"] = float(meta["Af"] / (15 * 2 * np.pi * meta["fc"] / 1000))
    if args.json:
        args.json.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
