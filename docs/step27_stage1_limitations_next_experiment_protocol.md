# Step 27.12-11U — Stage 1 Evaluation Limitations and Next Experiment Design

## Status

Protocol drafting in progress. No new experiments executed.

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

## Next Action

Define experiment inputs, metrics, and acceptance checks
before implementation.
