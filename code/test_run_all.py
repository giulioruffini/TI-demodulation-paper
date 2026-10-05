"""Regression checks for figure selection and cache-safe execution; no ODE runs."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import run_all


def labels(figures, from_cache=False):
    return [step[0] for step in run_all.resolve_steps(figures, from_cache)]


class FigurePlanTests(unittest.TestCase):
    def test_resonance_includes_stable_producer_and_plot(self):
        self.assertEqual(labels(['fig_resonance']),
                         ['data: resonance stable', 'rerun_resonance'])

    def test_concept_includes_uncommitted_analysis(self):
        self.assertEqual(labels(['fig_concept']), ['data: analyses_v2', 'figures_v2'])

    def test_shared_generators_run_once(self):
        self.assertEqual(labels(['fig_concept', 'fig_carrier_independence']),
                         ['data: analyses_v2', 'figures_v2'])

    def test_qif_selects_published_two_tone_data(self):
        self.assertEqual(labels(['fig_qif_raster_twotone']),
                         ['data: qif_raster twotone', 'make_qif_figs'])

    def test_qif_regimes_include_both_amplitudes_and_carrier_controls(self):
        self.assertEqual(labels(['fig_qif_regimes']),
                         ['data: qif_raster twotone', 'data: qif_raster amplitude10',
                          'data: carrier controls', 'make_qif_regimes_fig'])
        self.assertEqual(labels(['fig_qif_regimes'], True), ['make_qif_regimes_fig'])
        self.assertEqual(run_all.CACHE_INPUTS['make_qif_regimes_fig'],
                         ('qif_raster_twotone.npz', 'qif_raster_twotone_a10.npz',
                          'ping_carrier_control_traces.npz'))

    def test_cache_mode_never_adds_producers(self):
        self.assertEqual(labels(['fig_resonance'], True), ['rerun_resonance'])
        with self.assertRaisesRegex(ValueError, 'No cache-only renderer'):
            run_all.resolve_steps(['fig_khz_direct'], from_cache=True)

    def test_khz_recomputation_plots_the_new_spectra(self):
        plan = run_all.resolve_steps(['fig_khz_twotone'])
        self.assertEqual([step[0] for step in plan],
                         ['data: khz_twotone', 'make_khz_twotone_fig'])
        output = plan[0][2][plan[0][2].index('--write') + 1]
        source = plan[1][2][plan[1][2].index('--input') + 1]
        self.assertEqual(source, output)
        self.assertNotEqual(source, 'khz_twotone.npz')

    def test_khz_cache_mode_uses_the_archived_spectra(self):
        plan = run_all.resolve_steps(['fig_khz_twotone'], from_cache=True)
        self.assertEqual([step[0] for step in plan], ['make_khz_twotone_fig'])
        self.assertEqual(plan[0][2], [])
        self.assertEqual(run_all.CACHE_INPUTS[plan[0][0]], ('khz_twotone.npz',))

    def test_unknown_figure_does_not_succeed_silently(self):
        with self.assertRaisesRegex(ValueError, 'No generator'):
            run_all.resolve_steps(['fig_typo'])

    def test_dry_run_has_no_filesystem_or_subprocess_effects(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / 'new-figures'
            with patch.object(run_all.subprocess, 'run') as run, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(run_all.main(['--only', 'fig_resonance', '--dry-run',
                                               '--figdir', str(output)]), 0)
                run.assert_not_called()
            self.assertFalse(output.exists())

    def test_missing_cache_fails_before_plotting_or_creating_output(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / 'new-figures'
            with patch.object(run_all, 'HERE', td), patch.object(run_all.subprocess, 'run') as run:
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as exc:
                        run_all.main(['--only', 'fig_resonance', '--from-cache', '--figdir', str(output)])
                self.assertEqual(exc.exception.code, 2)
                run.assert_not_called()
            self.assertFalse(output.exists())

    def test_failed_producer_prevents_plotting_stale_cache(self):
        with tempfile.TemporaryDirectory() as td:
            # A stale cache must not let a failed recomputation look successful.
            (Path(td) / 'sweep_hi_stable.npz').write_bytes(b'stale')
            with patch.object(run_all, 'HERE', td), patch.object(run_all.subprocess, 'run') as run:
                run.return_value.returncode = 1
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(run_all.main(['--only', 'fig_resonance', '--figdir', td]), 1)
                self.assertEqual(run.call_count, 1)
                self.assertEqual(run.call_args.args[0][-1], 'stable')


if __name__ == '__main__':
    unittest.main()
