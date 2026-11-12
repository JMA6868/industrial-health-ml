# Step 27.12-11U — Stage 1 Evaluation Limitations and Next Experiment Design

## Status

U1 and U2 completed; U3 protocol defined. No U3 experiments executed.

## Objective

Assess limitations of the frozen CWRU Stage 1 RMS detector
and design reproducible diagnostic stress tests.

## Frozen Baseline

- Dataset: CWRU only.
- Target sampling rate: 12000 Hz.
- Window size: 1200 samples.
- Window step: 600 samples.
- RMS threshold: 0.07467624803042527.
- Window anomaly: RMS > threshold.
- Recording anomaly: anomalous window fraction > 0.05.
- Existing descriptive results: 45/45 Fault detections;
  0/2 evaluated Normal false alarms.

## Planned Investigations

1. Normal amplitude and false-alarm sensitivity.
2. Fault attenuation and missed-detection sensitivity.
3. Sequential alarm persistence analysis.
4. Observation-start-to-first-alarm timing.

## Scientific Boundaries

- Do not change the frozen baseline.
- Do not retune thresholds using evaluation recordings.
- Simulated amplitude changes are not new physical experiments.
- Online alarm rules must be evaluated separately.
- No true fault-onset timing is available.
- No independent cross-bearing generalization claim.
- Preserve earlier experiment results and data-use history.

## Experiment U1 — Normal Amplitude Stress Test

### Research Question

How sensitive is the frozen RMS detector to increases
in vibration amplitude from Normal recordings?

### Inputs

- Normal evaluation recordings: 99, 100.
- Amplitude scales: 1.00, 1.05, 1.10, 1.20, 1.50.
- Use existing harmonized RMS window sequences.
- Do not modify Normal training recordings 97 and 98.

### Procedure

1. Load original RMS window sequences.
2. Multiply RMS values by each fixed amplitude scale.
3. Apply the unchanged frozen RMS threshold.
4. Calculate the anomalous-window fraction.
5. Apply the unchanged recording-level 5% rule.

### Metrics

- Total windows.
- Anomalous windows.
- Anomalous-window fraction.
- Recording-level false-alarm outcome.
- First tested amplitude scale causing a false alarm.

### Interpretation

Amplitude scaling is a mathematical stress test.
It does not represent a new physical operating condition
or independent validation of real-world robustness.

## Experiment U2 — Fault Attenuation Stress Test

### Research Question

How does uniform fault-signal attenuation affect
the frozen Stage 1 recording-level detection rate?

### Inputs

- All 45 previously evaluated CWRU Fault recordings.
- Original 17 and additional 28 recording IDs are fixed
  in the Step 27.12-11Q evaluation protocol.
- Amplitude scales: 1.00, 0.75, 0.50, 0.25.
- Use existing harmonized RMS window sequences.

### Procedure

1. Load each recording's RMS window sequence.
2. Apply each fixed positive amplitude scale.
3. Use the unchanged frozen RMS threshold.
4. Apply the unchanged recording-level 5% rule.
5. Aggregate detection outcomes across all 45 recordings.
6. Summarize outcomes by fault type, diameter, and load.

### Metrics

- Total Fault recordings: 45.
- Detected and missed recording counts.
- Recording-level detection rate at each scale.
- Per-recording anomaly fractions.
- Detection rates by fault type, diameter, and motor load.

### Scientific Boundaries

- Diagnostic mathematical sensitivity analysis only.
- These are previously evaluated Fault recordings.
- Do not claim independent generalization.
- Do not recalibrate or optimize the frozen threshold.
- Do not treat scaled recordings as independent samples.
- Compare with Step 27.12-11R without replacing its results.

## Experiment U3 — Sequential Alarm Analysis

### Research Question

How does the required number of consecutive anomalous
windows affect alarm outcomes and observation-start timing?

### Inputs

- CWRU Normal evaluation recordings: 99, 100.
- All 45 previously evaluated Fault recordings.
- Original harmonized RMS window sequences.
- Frozen RMS threshold: 0.07467624803042527.
- Experimental persistence values: K = 1, 3, 5.

### Alarm Rule

An alarm occurs when K consecutive windows satisfy
RMS > frozen threshold.

Report only the first alarm per recording.

### Timing Definition

- Sampling rate: 12000 Hz.
- Window duration: 100 ms.
- Window step: 50 ms.
- First window ends at 100 ms.
- A run of K anomalies starting at window zero
  can trigger at 100 + 50 * (K - 1) ms.

### Metrics

- Alarm outcomes for each K.
- Normal recordings with alarms.
- Fault recordings with alarms.
- First alarm window index.
- Observation-start-to-first-alarm time.
- Comparison with frozen offline recording decisions.

### Scientific Boundaries

- Experimental online alarm strategy only.
- Do not modify the frozen offline 5% rule.
- Do not recalibrate the RMS threshold.
- No true fault-onset labels are available.
- Alarm timing excludes processing and communication delays.
- Overlapping windows are correlated observations.
- Results are descriptive, not independent generalization.

## Experiment U4 — Observation-Start Timing

### Research Question

How sensitive are sequential alarm outcomes and timing
to the starting position of the observation window?

### Inputs

- CWRU Normal evaluation recordings: 99, 100.
- All 45 previously evaluated Fault recordings.
- Frozen RMS threshold: 0.07467624803042527.
- Observation start indices: 0, 10, 50, 100.
- Experimental persistence values: K = 1, 3, 5.
- Expected evaluations: 564.

### Procedure

For each recording and observation start index:

1. Preserve the original ordered RMS window sequence.
2. Select the suffix beginning at the start index.
3. Reset the consecutive anomaly counter.
4. Apply the experimental K-consecutive alarm rule.
5. Record alarm outcome and first alarm position.
6. Calculate elapsed time relative to the new observation
   start using original window geometry.

### Timing Definition

For a first alarm at absolute window index j
and observation start window index s:

Elapsed time = ((j - s) * 600 + 1200) / 12000 seconds.

The first available complete window ends 100 ms
after the selected observation start.

### Metrics

- Alarm coverage by start index and K.
- Normal recordings with alarms.
- Fault recordings with alarms.
- First alarm timing: minimum, mean, maximum.
- Fault recordings with no alarm.
- Differences from U3 start-index-zero results.

### Scientific Boundaries

- Observation start is not a physical fault-onset timestamp.
- Window suffixes are not independent recordings.
- Existing CWRU recordings only; no new physical experiments.
- Do not retune the RMS threshold or frozen offline rule.
- Timing excludes computation and communication latency.
- Overlapping windows are correlated.
- No independent cross-bearing generalization claim.

## Next Action

Define experiment inputs, metrics, and acceptance checks
before implementation.
