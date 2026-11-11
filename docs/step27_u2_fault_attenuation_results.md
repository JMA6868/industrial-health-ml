# Step 27.12-11U — Experiment U2 Results

## Status

Completed diagnostic fault-attenuation analysis.

## Frozen Configuration

- CWRU Fault recordings: 45.
- RMS threshold: 0.07467624803042527.
- Recording anomaly fraction: strictly > 0.05.
- Amplitude scales: 1.00, 0.75, 0.50, 0.25.
- No threshold recalibration.

## Recording-Level Detection

| Scale | Detected | Missed | Detection Rate |
|---|---:|---:|---:|
| 1.00 | 45/45 | 0 | 100.00% |
| 0.75 | 45/45 | 0 | 100.00% |
| 0.50 | 41/45 | 4 | 91.11% |
| 0.25 | 32/45 | 13 | 71.11% |

## Missed Recording IDs

- 1.00: []
- 0.75: []
- 0.50: [119, 197, 224, 225]
- 0.25: [118, 119, 120, 121, 156, 169, 185, 197, 222, 223, 224, 225, 248]

## Detection by Fault Condition

| Condition | Recordings | 0.50x Detected | 0.25x Detected |
|---|---:|---:|---:|
| Ball | 13 | 10/13 (76.92%) | 4/13 (30.77%) |
| Inner Race | 13 | 13/13 (100.00%) | 12/13 (92.31%) |
| Outer Race 6:00 | 9 | 8/9 (88.89%) | 8/9 (88.89%) |
| Outer Race 3:00 | 5 | 5/5 (100.00%) | 4/5 (80.00%) |
| Outer Race 12:00 | 5 | 5/5 (100.00%) | 4/5 (80.00%) |

Ball Fault recordings showed the largest detection-rate
decrease under strong amplitude attenuation.

This observation does not establish that Ball Faults are
intrinsically harder to detect across physical bearings.

## Detection by Fault Diameter

| Diameter | Recordings | 0.50x Detected | 0.25x Detected |
|---|---:|---:|---:|
| 0.007 in | 14 | 13/14 (92.86%) | 9/14 (64.29%) |
| 0.014 in | 3 | 2/3 (66.67%) | 0/3 (0.00%) |
| 0.021 in | 20 | 18/20 (90.00%) | 15/20 (75.00%) |
| 0.028 in | 8 | 8/8 (100.00%) | 8/8 (100.00%) |

The 0.028-inch group differs in bearing manufacturer
and defect depth from smaller-defect groups.

Diameter alone cannot explain the observed differences.

## Detection by Motor Load

| Load | Recordings | 0.50x Detected | 0.25x Detected |
|---|---:|---:|---:|
| 0 HP | 15 | 14/15 (93.33%) | 9/15 (60.00%) |
| 1 HP | 10 | 9/10 (90.00%) | 8/10 (80.00%) |
| 2 HP | 10 | 9/10 (90.00%) | 7/10 (70.00%) |
| 3 HP | 10 | 9/10 (90.00%) | 8/10 (80.00%) |

The 0 HP group contains five additional recordings
and has a different fault composition from other loads.

These results do not establish a causal load effect.

## Scientific Limitations

- Mathematical amplitude stress test only.
- Previously evaluated CWRU fault recordings.
- Scaled signals are not independent samples.
- No cross-bearing generalization claim.
- Frozen Stage 1 baseline remains unchanged.

## Next Action

U2 grouped analysis completed. Review and commit U1/U2 results, then proceed to sequential alarm analysis and observation-start timing.
