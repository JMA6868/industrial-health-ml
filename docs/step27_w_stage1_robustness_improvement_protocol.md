# Step 27.12-11W — Stage 1 Robustness Improvement Strategy

## Status

Protocol drafted. No new detector implementation
or improvement experiment completed.

## Objective

Identify candidate improvements to the frozen Stage 1
RMS detector while preserving evaluation integrity.

## Existing Evidence

### Normal Amplitude Sensitivity

- Recording 97 critical scale: 1.002744124.
- Recording 98 critical scale: 1.164206236.
- Recording 99 critical scale: 1.257245490.
- Recording 100 critical scale: 1.237108443.
- Recording 97 and 98 are calibration recordings.
- Recording 99 and 100 were previously evaluated.

### Fault Attenuation Sensitivity

- Original Fault detection: 45/45.
- Detection at scale 0.75: 45/45.
- Detection at scale 0.50: 41/45.
- Detection at scale 0.25: 32/45.

### Sequential Alarm Behavior

- Experimental persistence values: K = 1, 3, 5.
- Fault alarms: 45/45 for all tested K.
- Evaluated Normal alarms: 0/2 for all tested K.
- Earliest alarm times: 100, 200, 300 ms.
- Synthetic transient sequences showed differences
  in short anomalous-run rejection.

## Candidate Improvement Strategies

### W1 — Normal-Only Normalization

Research whether normalization can reduce sensitivity
to amplitude changes in otherwise Normal signals.

Candidate methods require a predefined fitting policy.

Risks:
- Removing physically meaningful fault amplitude.
- Adapting to an already faulty condition.
- Leakage from evaluated recordings.

### W2 — Multi-Feature Anomaly Detection

Investigate complementary time-domain or frequency-domain
features rather than relying on RMS alone.

Potential features include:
- Crest factor.
- Kurtosis.
- Selected spectral features.

Risks:
- Increased complexity without measurable benefit.
- Unstable features under changing operating conditions.
- Feature selection based on previously evaluated results.

### W3 — Alarm Persistence

Investigate whether persistence improves robustness
against transient anomalies without unacceptable delay.

Risks:
- Delayed alarms.
- Missed short-duration abnormal events.
- Correlation from overlapping RMS windows.

## Evaluation Integrity

- CWRU only.
- Preserve the existing frozen RMS baseline.
- Do not recalibrate the baseline on evaluated recordings.
- Do not treat existing recordings as new untouched holdouts.
- Separate development experiments from final independent tests.
- Define fitting data and selection rules before evaluation.
- Use recording-level summaries and report dataset limitations.
- Do not claim physical-bearing-independent generalization
  without verified independent bearing identities.
- Synthetic perturbations are not physical experiments.

## Proposed Evaluation Metrics

- Normal recording-level false alarms.
- Fault recording-level detection coverage.
- Performance under predefined amplitude scaling.
- Performance under predefined fault attenuation.
- Observation-start-to-alarm timing.
- Computational complexity and reproducibility.

## Decision Gate

Before implementing a candidate improvement:

1. Specify its mechanism and expected benefit.
2. Identify exactly which recordings may be used for fitting.
3. Specify hyperparameters without consulting evaluation results.
4. Define a reproducible baseline comparison.
5. State what the available dataset cannot establish.

## W1 Finding — Fixed Global Standardization

### Method

Use only Normal calibration recordings 97 and 98
to estimate a fixed RMS mean and standard deviation.

Transform both the RMS values and frozen threshold
using the same positive standard deviation.

No evaluated recording was used to fit parameters.

### Results

- Training RMS mean: 0.064944584.
- Training RMS standard deviation: 0.005060496.
- Frozen threshold in standardized space: 1.923065377.
- Evaluated recording IDs: 97, 98, 99, 100, 105, 197, 3008.
- Total evaluated windows: 1305.
- All raw and standardized window decisions matched.

### Engineering Conclusion

Fixed global standardization with a consistently
transformed threshold is decision-equivalent to
the frozen RMS detector.

It is not a meaningful robustness improvement
and should not be introduced as a new detector.

### Limitations

- This verifies fixed affine standardization only.
- It does not evaluate per-condition normalization.
- It does not evaluate adaptive reference baselines.
- No new independent CWRU evaluation was performed.
- Frozen Stage 1 baseline remains unchanged.

## W1 Strategy Screening

### Fixed Global Standardization

Decision: Do not implement as a robustness improvement.

Reason:
A fixed positive affine transformation with a consistently
transformed threshold preserves all RMS anomaly decisions.

### Per-Recording Normalization

Decision: Defer as a detection strategy.

Potential benefit:
May reduce sensitivity to recording-level amplitude variation.

Risks:
- Fault-induced amplitude changes may be normalized away.
- Fitting on the evaluated recording creates adaptation
  to the unknown condition being diagnosed.
- Current CWRU evidence cannot establish reliability.

### Healthy-Reference Normalization

Decision: Retain as a conditional research candidate.

Potential benefit:
A separately established healthy reference may help
account for known operating-condition differences.

Requirements:
- Healthy reference data identified before evaluation.
- Reference parameters fitted using permitted data only.
- Explicit load/speed matching or unknown-condition handling.
- No adaptation using potentially faulty evaluation data.
- Fair comparison with the frozen RMS baseline.
- Independent validation before deployment claims.

### W1 Recommendation

Do not implement a new normalization detector yet.

First determine whether the available healthy training
recordings can support a meaningful reference strategy.

Normal recordings 97 and 98 cover only 0 HP and 1 HP.
Normal recordings 99 and 100 have already been evaluated
and must not be treated as untouched training data
for an independently validated improvement.

## W1 Final Decision — Healthy Reference Feasibility

### CWRU Load Coverage Audit

| Motor Load | Normal Recordings | Fault Recordings |
|---|---:|---:|
| 0 HP | 1 | 15 |
| 1 HP | 1 | 10 |
| 2 HP | 1 | 10 |
| 3 HP | 1 | 10 |
| Total | 4 | 45 |

### Available Normal Data

- Recording 97: 0 HP, original calibration data.
- Recording 98: 1 HP, original calibration data.
- Recording 99: 2 HP, previously evaluated.
- Recording 100: 3 HP, previously evaluated.

Each motor-load condition has only one Normal recording.

### Engineering Assessment

The current dataset does not provide sufficient
independent healthy-reference observations to establish
a reliable load-matched normalization strategy.

Original calibration data cover only 0 HP and 1 HP.
Previously evaluated Normal recordings must not be
reclassified as untouched training data.

Normal/Fault acquisition and preprocessing differences
remain unresolved.

### W1 Final Decision

- Fixed global standardization: reject as an improvement.
- Per-recording normalization: defer.
- Healthy-reference normalization: defer pending stronger data.

No new normalization detector will be implemented
in Step 27.12-11W.

This is a feasibility decision, not proof that
normalization cannot work on other datasets.

### Next Research Direction

Proceed to W2 — Multi-Feature Anomaly Detection.

Audit existing feature extraction and training-only
calibration capabilities before proposing a new detector.

Do not tune candidate methods using previously
evaluated recordings and then claim independent
holdout performance.

## W2 Finding — Harmonized RMS and Crest Factor

### Method

Extract RMS and Crest Factor from identical 12 kHz
harmonized CWRU signal windows.

- Window size: 1200 samples.
- Window step: 600 samples.
- Frozen RMS threshold: 0.07467624803042527.
- Crest Factor P99 threshold: 4.156405692.
- CF threshold fitted using Normal 97 and 98 only.
- Recording anomaly fraction strictly greater than 0.05.
- Experimental combined rule: RMS anomaly OR CF anomaly.

### Software Verification

- Harmonized multifeature module implemented.
- 14 dedicated unit tests passed.
- Seven recordings verified for RMS baseline consistency.
- Existing frozen RMS detector left unchanged.

### Normal Recording Results

| Recording | RMS Alarm | RMS+CF OR Alarm |
|---|---|---|
| 97 | No | No |
| 98 | No | No |
| 99 | No | No |
| 100 | No | Yes |

Recording 100 produced 14/201 CF-anomalous windows,
exceeding the 5% recording-level alarm threshold.

### Fault Attenuation Results

| Scale | RMS-only | RMS+CF OR | Recovered Faults |
|---|---:|---:|---:|
| 1.00 | 45/45 | 45/45 | 0 |
| 0.75 | 45/45 | 45/45 | 0 |
| 0.50 | 41/45 | 42/45 | 1 |
| 0.25 | 32/45 | 39/45 | 7 |

Recovered at scale 0.50:
- Recording 224.

Recovered at scale 0.25:
- Recordings 156, 169, 185, 222, 223, 224, 248.

### Interpretation

Crest Factor is invariant under positive uniform
amplitude scaling for nonzero signals.

The experimental OR rule recovered some attenuated
Fault recordings missed by RMS-only detection.

However, the same OR rule introduced a Normal recording
false alarm on Recording 100.

This illustrates a trade-off between weak-fault
detection and Normal alarm stability.

### Scientific Limitations

- All recordings were previously examined.
- Results are exploratory, not independent holdout scores.
- Uniform amplitude attenuation is simulated.
- Normal recordings 97 and 98 were used for calibration.
- Normal recordings 99 and 100 were previously evaluated.
- No independent physical-bearing generalization established.
- CF P99 and RMS P99 do not guarantee equal false-alarm rates.
- Overlapping windows are correlated.
- Acquisition and preprocessing confounding remains.

### W2 Decision

Retain RMS + Crest Factor as an exploratory candidate.

Do not replace the frozen Stage 1 RMS detector.

Do not tune CF thresholds against Recording 100 or
the attenuated Fault outcomes and then present the
result as an independent evaluation.

## W3 Finding — Online Alarm Persistence Trade-off

### Method

Compare experimental online alarms using RMS-only
and RMS + Crest Factor OR window-anomaly rules.

- Frozen RMS threshold: 0.07467624803042527.
- CF P99 threshold: 4.156405692.
- CF calibrated using Normal 97 and 98 only.
- Persistence values: K = 1, 3, 5.
- Simulated Fault amplitude scales: 1.00, 0.50, 0.25.
- A recording alarms if any K consecutive windows
  satisfy the chosen window-anomaly rule.

Online persistence is distinct from the frozen
offline recording-level anomaly fraction > 0.05 rule.

### Normal Recording Online Alarms

| K | RMS-only | RMS + CF OR |
|---|---:|---:|
| 1 | 1/4 | 4/4 |
| 3 | 0/4 | 1/4 |
| 5 | 0/4 | 0/4 |

- K=1 RMS-only alarmed on Recording 97.
- K=3 OR alarmed on Recording 100.
- K=5 produced no Normal recording alarms
  in this limited evaluated sample.

### Fault Recording Online Alarms

| Scale | K | RMS-only | RMS + CF OR |
|---|---:|---:|---:|
| 1.00 | 1 | 45/45 | 45/45 |
| 1.00 | 3 | 45/45 | 45/45 |
| 1.00 | 5 | 45/45 | 45/45 |
| 0.50 | 1 | 42/45 | 45/45 |
| 0.50 | 3 | 40/45 | 40/45 |
| 0.50 | 5 | 40/45 | 40/45 |
| 0.25 | 1 | 35/45 | 44/45 |
| 0.25 | 3 | 29/45 | 39/45 |
| 0.25 | 5 | 28/45 | 38/45 |

### Key Findings

- Crest Factor adds some weak-fault detection coverage
  under simulated amplitude attenuation.
- Increasing K reduces Normal alarms in the tested
  recordings but can lose weak-fault detections.
- K=5 removes observed Normal alarms in this sample
  while detecting 38/45 attenuated Fault recordings
  at scale 0.25.
- This observation is not evidence that K=5 is
  an independently validated optimal setting.

### Scientific Limitations

- Previously evaluated CWRU recordings reused.
- All Normal recordings include calibration or
  previously evaluated data.
- Simulated attenuation is not a physical experiment.
- K values compared exploratorily, not independently
  selected and validated.
- Windows overlap and are statistically dependent.
- Online results are not comparable to offline
  >5% decisions without accounting for rule changes.
- No field false-alarm rate or true fault-onset delay
  can be established from these recordings.
- Acquisition and bearing-identity confounding remains.

### W3 Decision

Retain persistence-based RMS + CF alarms as an
exploratory research direction.

Do not replace or retune the frozen Stage 1 baseline.

Independent normal-condition and fault-transition
data are needed before selecting a deployment K.

## Next Action

Audit candidate normalization methods and available
training-only data before choosing an implementation.
