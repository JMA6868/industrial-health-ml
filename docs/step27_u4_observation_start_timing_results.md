# Step 27.12-11U — Experiment U4 Results

## Status

Completed observation-start timing analysis and verification.

## Research Question

How sensitive are sequential alarm coverage and timing
to the selected observation starting position?

## Configuration

- Dataset: CWRU only.
- Normal evaluation recordings: 99, 100.
- Fault recordings: 45 previously evaluated recordings.
- Frozen RMS threshold: 0.07467624803042527.
- Observation start window indices: 0, 10, 50, 100.
- Experimental persistence values: K = 1, 3, 5.
- Window duration: 100 ms.
- Window step: 50 ms.
- Total evaluations: 47 recordings x 4 starts x 3 K = 564.
- Frozen offline 5% rule unchanged.

## Alarm Coverage

Fault recordings with alarms:

| Start Index | K=1 | K=3 | K=5 |
|---|---:|---:|---:|
| 0 | 45/45 | 45/45 | 45/45 |
| 10 | 45/45 | 45/45 | 45/45 |
| 50 | 45/45 | 45/45 | 45/45 |
| 100 | 45/45 | 45/45 | 45/45 |

Normal recordings with alarms:

- 0/2 for every observation start and persistence setting.
- No missed Fault recordings in any tested configuration.

## First Alarm Timing

For every tested observation start:

| K | Minimum | Mean | Maximum |
|---|---:|---:|---:|
| 1 | 0.100 s | 0.100 s | 0.100 s |
| 3 | 0.200 s | 0.200 s | 0.200 s |
| 5 | 0.300 s | 0.300 s | 0.300 s |

All 45 Fault recordings reached the alarm condition at
the earliest possible time for every tested start and K.

## Timing Definition

For observation start index s and first alarm absolute
window index j:

Elapsed time = ((j - s) * 600 + 1200) / 12000 seconds.

The anomaly counter is reset at each new observation start.

## Verification

- 14 U4 unit tests passed.
- 564 CWRU recording/start/K evaluations completed.
- All 564 alarm outcomes and timing assertions passed.
- Relative and absolute alarm window indices verified.
- All selected observation starts and K values verified.

## Interpretation

Changing the observation start among indices
0, 10, 50, and 100 did not change alarm coverage
or the earliest possible observation-relative alarm
time in the evaluated recordings.

These results are consistent with the strong anomaly
separation observed in earlier Stage 1 experiments.

## Scientific Limitations

- Observation start is not a physical fault-onset timestamp.
- No actual fault-onset-to-detection delay was measured.
- The 564 evaluations reuse the same 47 recordings.
- Window suffixes are not independent physical experiments.
- Only two Normal evaluation recordings were included.
- Overlapping RMS windows are correlated.
- Processing and communication delays are excluded.
- No field false-alarm rate or optimal K established.
- Acquisition differences and bearing-domain confounding
  remain unresolved.
- No independent cross-bearing generalization claim.

## Engineering Conclusion

On these CWRU recordings, increasing alarm persistence
from K=1 to K=5 adds 200 ms of minimum observation-relative
waiting time without changing observed alarm coverage.

This result does not establish how the system would behave
under changing operating conditions, emerging faults,
or measured transient interference.

## Next Action

Complete U3/U4 test-suite verification, review documentation,
and commit the experimental results.
