# Step 27.12-11V — Normal Operating-Condition Analysis

## Status

Initial descriptive analysis and Recording 97 boundary
verification completed.

## Research Question

How does the frozen Stage 1 RMS detector behave across
the available CWRU Normal operating loads?

## Dataset

| Recording | Motor Load | Data Role | Windows |
|---|---:|---|---:|
| 97 | 0 HP | Calibration | 100 |
| 98 | 1 HP | Calibration | 200 |
| 99 | 2 HP | Previously evaluated | 201 |
| 100 | 3 HP | Previously evaluated | 201 |

## Frozen Detector

- RMS threshold: 0.07467624803042527.
- Window anomaly: RMS > threshold.
- Recording anomaly: anomalous window fraction > 0.05.
- Window size: 1200 samples.
- Window step: 600 samples.
- Sampling rate: 12000 Hz.
- Threshold and recording-level rule unchanged.

## Normal RMS Distribution

| ID | Load | Mean RMS | Max RMS | P99 RMS | Anomalous Windows |
|---|---|---:|---:|---:|---:|
| 97 | 0 HP | 0.071742 | 0.074949 | 0.074828 | 3/100 |
| 98 | 1 HP | 0.061546 | 0.067000 | 0.064771 | 0/200 |
| 99 | 2 HP | 0.057345 | 0.060526 | 0.060350 | 0/201 |
| 100 | 3 HP | 0.057900 | 0.062031 | 0.060916 | 0/201 |

## Threshold Margin and Critical Scale

| ID | Load | Max Margin | P95 Margin | P99 Margin | Critical Scale |
|---|---|---:|---:|---:|---:|
| 97 | 0 HP | -0.000273 | +0.000200 | -0.000152 | 1.002744 |
| 98 | 1 HP | +0.007677 | +0.010530 | +0.009905 | 1.164206 |
| 99 | 2 HP | +0.014150 | +0.015280 | +0.014327 | 1.257245 |
| 100 | 3 HP | +0.012645 | +0.014313 | +0.013760 | 1.237108 |

Margin = frozen RMS threshold - observed RMS statistic.

Critical scale is the equality boundary for the first
recording-level alarm. Strictly exceeding it is required.

## Recording 97 Boundary Verification

| Scale | Anomalous Windows | Recording Alarm |
|---|---:|---|
| 1.000000000 | 3/100 | No |
| 1.002743121 | 5/100 | No |
| 1.002745126 | 6/100 | Yes |
| 1.005000000 | 7/100 | Yes |
| 1.010000000 | 11/100 | Yes |

- Critical scale boundary: 1.002744124.
- Required anomalous windows: 6 of 100.
- Uniform amplitude increase at the boundary: about 0.2744%.
- The frozen detector was not recalibrated.

## Main Findings

1. Normal RMS distributions differ across the four
   available motor-load recordings.
2. Recording 97 has the smallest recording-level
   false-alarm margin under uniform amplitude scaling.
3. Even calibration recordings may include individual
   anomalous windows without a recording-level alarm.
4. Mean RMS does not decrease monotonically from
   0 HP through 3 HP in these four recordings.

## Scientific Limitations

- One Normal recording per motor-load setting.
- Motor load is confounded with recording identity and
  potentially other experimental conditions.
- Recordings 97 and 98 were used for threshold calibration.
- Recordings 99 and 100 were evaluated previously.
- No untouched independent Normal holdout is available.
- Uniform scaling is a simulated perturbation, not a
  measured physical operating-condition change.
- No causal motor-load effect can be established.
- No industrial field false-alarm rate is established.
- Overlapping windows are correlated observations.
- Existing acquisition and preprocessing confounding remains.

## Engineering Implication

The Stage 1 RMS detector can have markedly different
recording-level alarm margins across Normal recordings.
Additional independent operating-condition data would
be needed to evaluate deployment robustness.

## Next Action

Review the analysis, add reproducibility checks,
and decide whether further experiments are justified
without tuning the frozen baseline on evaluated data.
