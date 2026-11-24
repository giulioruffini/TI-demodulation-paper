"""Arithmetic checks for the referee assessment; no simulation or cache changes."""
import json
import math


def access(f_hz, tau_s=0.0002):
    return 1 / math.sqrt(1 + (2 * math.pi * f_hz * tau_s) ** 2)


def ratio(low, high):
    return math.prod(access(f) for f in high) / math.prod(access(f) for f in low)


results = {
    'tau_s': 0.0002,
    'narrowband_9_over_1': ratio((1000, 1000), (9000, 9000)),
    'missey_abstract_pairs': ratio((1000, 1130), (9000, 9130)),
    'missey_methods_pairs': ratio((1300, 1430), (9000, 9130)),
    'illustrative_budget': [],
}
for frequency in (1000, 2000, 9000):
    polarization = 0.5 * 0.5 * access(frequency)
    source = -0.1508 * polarization**2 / 2
    results['illustrative_budget'].append({
        'frequency_hz': frequency,
        'per_carrier_field_V_m': 0.5,
        'coupling_mV_per_V_m': 0.5,
        'post_access_polarization_mV': polarization,
        'signed_DC_and_beat_source_s_inverse_narrowband': source,
        'equivalent_direct_polarization_microvolts': 1000 * source / 0.4745,
    })
print(json.dumps(results, indent=2))
