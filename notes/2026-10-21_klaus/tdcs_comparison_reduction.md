# TI steady source vs tDCS: the reduction behind the 2–5% (reply to Kaiti, 2026-10-21)

Numbers check: JR sigmoid (rho 0.56/mV, v0 6 mV, e0 2.5/s) at v* = 8.30 mV gives
Sig' = 0.4745, Sig'' = -0.1508, |Sig''| eps / (2 Sig') = 0.159 eps/mV: 1.6% at 0.1 mV,
4.8% at 0.3 mV. Matches sec:dc.

Kaiti's point stands: the comparison is at equal amplitude in the sigmoid-input coordinate s,
and TI (AIS, kHz) and tDCS (soma/dendrites, DC) convert physical polarization into s through
different compartments. The paper already conditions on "the polarization reaching the same
sigmoid" and "inputs at the same entry point", and already says access differs between DC, the
beat, and the carriers; the compartment dimension is the one addition.

Her interpretation sentence is physically right (AIS polarization shifts the distance between
somatic potential and spike threshold; no back-propagation needed) and answers the question a
reader asks at eq:coupling when the soma is shut at kHz. Two adjustments:

1. Put it in the paper's variables: Sig(v+s) with s at the AIS is Sig with threshold v0 - s.
2. Merge with the existing calibration clause after eq:doors ("their coupling and response
   time require calibration in the preparation") so calibration is said once.

Proposed text, replacing "Fast axonal compartments motivate ... in the preparation." (l. ~349):

  Fast axonal compartments motivate the direct-coupling approximation
  $\lambda_f\approx\lambda_0$. For coupling at the AIS, the additive input $s$
  shifts the distance between the somatic potential and the spike threshold:
  $\Sig(v+s)$ is the same curve with threshold $v_0-s$. No backward transmission
  to the soma is required. Converting the local AIS polarization into $s$, and
  the compartment's response time, require calibration in the preparation.

Proposed addition to the comparison paragraph's last sentence (l. ~740):
  "... because access differs between DC, the beat frequency, and the carriers,
  and between the compartments through which each enters."
