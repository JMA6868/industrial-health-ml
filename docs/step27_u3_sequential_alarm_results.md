# Step 27.12-11U — Experiment U3 Results

## Status

Completed sequential alarm analysis and timing verification.

## Configuration

- Dataset: CWRU only.
- Normal evaluation recordings: 99, 100.
- Fault recordings: 45 previously evaluated recordings.
- Frozen RMS threshold: 0.07467624803042527.
- Experimental persistence values: K = 1, 3, 5.
- Window duration: 100 ms.
- Window step: 50 ms.
- Total evaluations: 141.
- Frozen offline 5% rule unchanged.

## Alarm Coverage

| K | Normal Alarms | Fault Alarms | No-Alarm Faults |
|---|---:|---:|---:|
| 1 | 0/2 | 45/45 | 0 |
| 3 | 0/2 | 45/45 | 0 |
| 5 | 0/2 | 45/45 | 0 |

## First Alarm Timing

| K | Min | Mean | Max |
|---|---:|---:|---:|
| 1 | 0.100 s | 0.100 s | 0.100 s |
| 3 | 0.200 s | 0.200 s | 0.200 s |
| 5 | 0.300 s | 0.300 s | 0.300 s |

All 45 Fault recordings alarmed at the earliest possible
time for each tested persistence value.

## Verification

- 14 U3 unit tests passed.
- All 141 recording/K evaluations completed.
- All alarm outcomes and timing assertions passed.
- First alarm index equals K - 1 for every Fault recording.
- No Normal evaluation recording triggered an alarm.

## Interpretation

Increasing K from 1 to 5 increased observation-start
alarm time from 100 ms to 300 ms without changing
alarm coverage in this evaluated CWRU subset.

This does not establish that K=1 is optimal for deployment.

## Scientific Limitations

- Experimental online alarm rule, not the frozen offline rule.
- No true fault-onset timestamps are available.
- Timing is measured relative to recording start.
- Processing and communication latency are excluded.
- Overlapping windows are correlated observations.
- Only two Normal evaluation recordings were available.
- No independent cross-bearing generalization claim.
- Transient interference rejection remains untested.

## Controlled Transient Interference Stress Test

### Method

Five synthetic RMS window sequences were constructed
using values below and above the frozen RMS threshold.

These sequences test sequential alarm logic only.
They are not new CWRU recordings or physical experiments.

### Results

| Synthetic Scenario | K=1 | K=3 | K=5 |
|---|---|---|---|
| No interference | No alarm | No alarm | No alarm |
| Single abnormal window | Alarm | No alarm | No alarm |
| Three consecutive anomalies | Alarm | Alarm | No alarm |
| Five consecutive anomalies | Alarm | Alarm | Alarm |
| Three separated anomalies | Alarm | No alarm | No alarm |

### Interpretation

K=1 responded to every scenario containing an abnormal window.

K=3 rejected isolated and separated anomalies but responded
to three or more consecutive abnormal windows.

K=5 required five consecutive abnormal windows.

Higher persistence can reject short abnormal-window sequences,
but it also increases the minimum time required to alarm
and can miss shorter genuine abnormal events.

### Limitations

- Synthetic window sequences, not measured interference.
- No physical disturbance duration can be inferred directly.
- Overlapping RMS windows are statistically dependent.
- No field false-alarm rate or optimal K established.

## Next Action

Design controlled transient-anomaly sequences to compare
persistence rules, then investigate observation-start timing.
