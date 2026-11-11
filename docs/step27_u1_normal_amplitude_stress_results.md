# Step 27.12-11U — Experiment U1 Results

## Status

Completed diagnostic normal-amplitude stress analysis.

## Experiment Configuration

- Dataset: CWRU only.
- Normal evaluation recordings: 99, 100.
- Sampling rate: 12000 Hz after harmonization.
- Window size: 1200 samples.
- Window step: 600 samples.
- Frozen RMS threshold: 0.07467624803042527.
- Recording alarm: anomalous window fraction > 0.05.
- Tested scales: 1.00, 1.05, 1.10, 1.20, 1.50.
- No threshold recalibration.

## Tested Amplitude Scales

| ID | Scale | Windows | Anomalous | Fraction | False Alarm |
|---|---:|---:|---:|---:|---|
| 99 | 1.00 | 201 | 0 | 0.0000 | No |
| 99 | 1.05 | 201 | 0 | 0.0000 | No |
| 99 | 1.10 | 201 | 0 | 0.0000 | No |
| 99 | 1.20 | 201 | 0 | 0.0000 | No |
| 99 | 1.50 | 201 | 201 | 1.0000 | Yes |
| 100 | 1.00 | 201 | 0 | 0.0000 | No |
| 100 | 1.05 | 201 | 0 | 0.0000 | No |
| 100 | 1.10 | 201 | 0 | 0.0000 | No |
| 100 | 1.20 | 201 | 0 | 0.0000 | No |
| 100 | 1.50 | 201 | 201 | 1.0000 | Yes |

## Critical False-Alarm Scales

The recording-level rule requires at least 11 anomalous
windows out of 201 to trigger a false alarm.

| ID | Boundary RMS | Critical Scale | Increase |
|---|---:|---:|---:|
| 99 | 0.059396712 | 1.257245 | 25.72% |
| 100 | 0.060363542 | 1.237108 | 23.71% |

Because the window rule uses strict RMS > threshold,
the critical scales are theoretical boundaries.
A slightly larger scale is required to trigger an alarm.

## Boundary Verification

- Recording 99: below 10/201 (False); above 11/201 (True).
- Recording 100: below 10/201 (False); above 11/201 (True).
- Both critical-scale boundary checks passed.

## Interpretation

The fixed RMS detector is sensitive to global signal
amplitude changes even when the original Normal recording
contains no known bearing fault.

The observed critical scales apply only to these two
recordings under the specified mathematical transformation.

## Scientific Limitations

- Amplitude scaling is a diagnostic mathematical test.
- It does not reproduce a new physical operating condition.
- Only two previously evaluated Normal recordings were used.
- These are not new independent holdout recordings.
- Results do not estimate real-world false-alarm rates.
- Physical-bearing and sensor-gain independence are unverified.
- No baseline threshold or model parameters were changed.

## Implementation

- src/stage1_normal_amplitude_stress.py
- tests/test_stage1_normal_amplitude_stress.py
- docs/step27_stage1_limitations_next_experiment_protocol.md

## Next Action

Review U1 results and design Experiment U2
for fault attenuation and missed-detection sensitivity.
