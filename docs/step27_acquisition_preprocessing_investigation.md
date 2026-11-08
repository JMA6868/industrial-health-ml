# Step 27.12-11S — CWRU Acquisition and Preprocessing Confound Investigation

## Status

Descriptive investigation of sampling-rate harmonization,
frequency-band energy, and RMS detection sensitivity.

The original frozen Stage 1 baseline remains unchanged.

## Dataset and Existing Pipeline

- 4 Normal recordings: 97, 98, 99, 100
- 45 Fault recordings
- Normal source sampling rate: 48 kHz
- Fault source sampling rate: 12 kHz
- Harmonized sampling rate: 12 kHz
- Window size: 1200 samples
- Step size: 600 samples
- Frozen RMS threshold: 0.07467624803042527
- Recording-level anomaly fraction threshold: strictly greater than 5%

Normal recordings 97 and 98 were used for calibration.
Normal recordings 99 and 100 were previously evaluated.

All analyzed signals use the Drive End channel.

## 1. Normal Resampling RMS Changes

The Normal signals were downsampled from 48 kHz to 12 kHz
using scipy.signal.resample_poly.

| Recording | Original RMS | Harmonized RMS | Change |
|---|---:|---:|---:|
| 97 | 0.073763968 | 0.071767512 | -2.71% |
| 98 | 0.066352043 | 0.061585394 | -7.18% |
| 99 | 0.064325396 | 0.057348885 | -10.85% |
| 100 | 0.065883867 | 0.057923579 | -12.08% |

These values are full-recording RMS measurements.

## 2. Original Normal High-Frequency Power

Welch PSD was used to estimate power above 6 kHz
in the original 48 kHz Normal signals.

| Recording | Power Above 6 kHz | Predicted RMS Drop | Actual RMS Drop |
|---|---:|---:|---:|
| 97 | 5.52% | 2.80% | 2.71% |
| 98 | 14.33% | 7.44% | 7.18% |
| 99 | 21.19% | 11.23% | 10.85% |
| 100 | 23.49% | 12.53% | 12.08% |

The predicted drops assume ideal removal of power above 6 kHz.

The close agreement supports high-frequency power attenuation
as an important explanation for the observed RMS reductions.

Welch PSD estimates and the actual resampling filter are not
identical to an ideal brick-wall filter.

## 3. Normal Window RMS Boundary Sensitivity

Using 100 ms windows at each sampling rate:

| Recording | Original 48 kHz Max RMS | Harmonized 12 kHz Max RMS |
|---|---:|---:|
| 97 | 0.076843927 | 0.074948803 |
| 98 | 0.071359820 | 0.066999517 |
| 99 | 0.067270165 | 0.060525792 |
| 100 | 0.069340870 | 0.062031160 |

The observed minimum Fault RMS at 12 kHz was 0.074981158.

- Original 48 kHz Normal vs 12 kHz Fault gap: -0.001862769
- Harmonized 12 kHz Normal vs 12 kHz Fault gap: +0.000032355

This is a preprocessing-sensitivity diagnostic, not a
same-bandwidth comparison of two independently calibrated models.

## 4. Frozen Threshold Applied to Original 48 kHz Normal

| Recording | Original 48 kHz Anomaly Fraction | Harmonized 12 kHz Fraction |
|---|---:|---:|
| 97 | 29.00% | 3.00% |
| 98 | 0.00% | 0.00% |
| 99 | 0.00% | 0.00% |
| 100 | 0.00% | 0.00% |

Recording 97 would be classified Abnormal under the original
12 kHz-calibrated threshold applied directly to its 48 kHz signal.

Recording 97 is a calibration recording, not an independent holdout.

## 5. Frequency-Band Power Comparison

The following values use harmonized 12 kHz signals and Welch PSD.

| Recording | Class | Power 0–3 kHz | Power 3–6 kHz |
|---|---|---:|---:|
| 97 | Normal | 30.86% | 69.14% |
| 98 | Normal | 56.90% | 43.10% |
| 99 | Normal | 59.14% | 40.86% |
| 100 | Normal | 61.76% | 38.24% |
| 105 | Fault | 59.57% | 40.43% |
| 185 | Fault | 36.50% | 63.50% |
| 197 | Fault | 23.71% | 76.29% |
| 224 | Fault | 29.84% | 70.16% |

High 3–6 kHz power fraction is not unique to Fault recordings.

Relative band-power fractions must not be confused with
absolute RMS amplitudes.

## 6. Diagnostic 3 kHz Low-pass Experiment

A sixth-order Butterworth low-pass filter with a 3 kHz
cutoff was applied using scipy.signal.sosfiltfilt
after harmonization to 12 kHz.

For recordings 97 and 197:

| Recording | Full-band RMS | Low-pass RMS | Change |
|---|---:|---:|---:|
| 97 | 0.071767512 | 0.040512921 | -43.55% |
| 197 | 0.100679227 | 0.049124566 | -51.21% |

Applying the original frozen threshold after low-pass
filtering produced:

- Normal 97: 0/100 anomalous windows; Normal
- Fault 197: 0/202 anomalous windows; Normal (missed Fault)

This demonstrates threshold sensitivity to preprocessing changes.
The original threshold was not calibrated for the low-pass pipeline.

## 7. Diagnostic Recalibration Using Normal Training Data

A separate diagnostic RMS P99 threshold was calibrated
using low-pass-filtered Normal recordings 97 and 98 only.

Diagnostic threshold: 0.050110350

Recording-level anomaly rule: fraction strictly greater than 5%.

Results across the existing 49 recordings:

- Fault recordings detected: 45/45
- Missed Fault recordings: none
- Normal evaluation false alarms: 0/2 (99 and 100)
- Fault 197 anomaly fraction: 38.61%
- Fault 223 anomaly fraction: 73.63%

All other evaluated Fault recordings had 100% anomalous windows.

These are descriptive results on previously available CWRU
recordings, not an independent untouched holdout evaluation.

The diagnostic threshold does not replace the original frozen threshold.

## 8. Window-Level Separation After Low-pass Filtering

- Maximum Normal window RMS: 0.050635063 (recording 98)
- Minimum Fault window RMS: 0.041269475 (recording 197)
- Low-pass separation gap: -0.009365587
- Original frozen pipeline gap: +0.000032355

Window-level RMS ranges overlap after low-pass filtering,
while the recording-level detector still identifies all
45 evaluated Fault recordings.

Thus, complete window-level separation is not required for
correct recording-level decisions under the 5% rule.

## 9. Scientific Limitations

1. Normal and Fault recordings originate from different
   source sampling-rate groups.
2. Resampling equalizes sample rates but does not establish
   identical original acquisition conditions.
3. Sensor gain, installation, and recording-condition
   equivalence have not been independently verified.
4. The 3 kHz low-pass analysis is a diagnostic alternative,
   not a replacement or independent evaluation of the baseline.
5. Calibration recordings 97 and 98 are not independent holdouts.
6. Recording-level outcomes are descriptive for this CWRU subset.
7. Overlapping windows are correlated observations.
8. Physical-bearing independence and cross-device generalization
   remain unverified.
9. Differences in relative spectral energy do not establish
   causal relationships with fault condition.

## Next Investigation

Verify official CWRU acquisition documentation and sensor
configuration where possible.

Investigate whether amplitude-based separation is affected by
measurement conditions, sensor scaling, and recording identity.

Preserve all frozen baseline experiments and historical results.
