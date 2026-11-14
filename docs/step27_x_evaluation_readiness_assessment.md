# Step 27.12-11X — Evaluation Readiness Assessment

## Overall Assessment

Research-ready and reproducible, but not independently
validated for industrial deployment.

## Scope

This assessment covers the existing CWRU-only
IndustrialSense AI Stage 1 evidence.

It does not introduce new experiments or models.

## Evidence Summary

### Software Verification

- Full automated regression suite: 326 passed.
- Data loading, feature extraction, thresholds,
  alarm decisions, and numerical edge cases are tested.
- Test success establishes specified software behavior,
  not physical fault-detection generalization.

### Historical Model Evaluations

Step 24:
- RMS threshold classifier with threshold 0.18.
- Threshold originated in earlier exploratory work.
- Holdout recordings: 100 and 108.
- Historical confusion matrix: TN=808, FP=0,
  FN=0, TP=203.

Step 26:
- StandardScaler + LogisticRegression.
- Configuration frozen before its final evaluation.
- Reused recordings 100 and 108, already seen
  during Step 24.
- Historical confusion matrix: TN=808, FP=0,
  FN=0, TP=203.

These are different models evaluated on the same
recording-level holdout, not two independent datasets.

### Current Frozen Stage 1 RMS Baseline

- Target sampling rate: 12000 Hz.
- Normal calibration recordings: 97 and 98.
- Frozen RMS P99 threshold: 0.07467624803042527.
- Recording anomaly fraction strictly greater than 0.05.
- Descriptive Fault detections: 45/45.
- Previously evaluated Normal alarms: 0/2.

The results are descriptive and do not provide
an untouched independent holdout for new variants.

### Robustness and Candidate Methods

- U1/V1: Normal amplitude sensitivity.
- U2: Fault attenuation and missed detections.
- U3/U4: Sequential alarms and observation-start timing.
- W1: Fixed standardization decision equivalence.
- W2: RMS + Crest Factor exploratory improvement
  under attenuation, with additional Normal alarm.
- W3: Online alarm persistence trade-offs.

No candidate method was selected as a validated
replacement for the frozen RMS baseline.

## Readiness Decision

| Dimension | Assessment |
|---|---|
| Software reproducibility | Supported by existing tests |
| Existing CWRU descriptive evaluation | Completed |
| Simulated robustness exploration | Completed |
| Recording-level split hygiene | Documented |
| Physical-bearing independence | Unverified |
| Untouched holdout for new variants | Unavailable locally |
| Real operating-condition robustness | Unverified |
| Measured fault-onset latency | Unavailable |
| Industrial deployment readiness | Not established |

## Principal Risks

1. Only four Normal recordings, with one per motor load.
2. All local recordings have been previously examined.
3. Original recording IDs do not establish bearing identity.
4. Normal and Fault acquisition conditions differ.
5. Overlapping windows create correlated observations.
6. Simulated scaling cannot replace measured disturbances.
7. Perfect historical scores reflect limited CWRU subsets.

## Recommendations

### Immediate

- Preserve the frozen RMS baseline.
- Keep candidate improvements explicitly exploratory.
- Document data exposure and acquisition limitations.
- Use qualified claims in README and presentations.

### Before Claiming Generalization

- Obtain genuinely independent physical-bearing data,
  with acquisition and label provenance.
- Include independent Normal recordings across loads.
- Pre-register model fitting and selection policies.
- Reserve a truly untouched final evaluation set.
- Report recording- or bearing-level uncertainty.

### Before Deployment Claims

- Validate on real equipment and operating shifts.
- Measure transient interference and field false alarms.
- Obtain fault-onset labels for detection latency.
- Evaluate reliability, monitoring latency,
  and operational response requirements.

## Recommended Presentation Statement

IndustrialSense AI implements a reproducible CWRU
bearing-anomaly detection workflow with 326 passing
automated tests. The frozen RMS detector identified
45/45 previously evaluated Fault recordings with
0/2 previously evaluated Normal recording alarms.
Controlled robustness studies exposed sensitivity
to amplitude shifts and alarm-design trade-offs.
Independent bearing-level and field validation
remain outstanding.

## Supporting Documents

- `docs/step27_x_evaluation_readiness_protocol.md`
- `docs/step27_x_data_exposure_inventory.md`
- `docs/step27_x_claim_to_evidence_matrix.md`
- `docs/step27_official_acquisition_metadata_audit.md`
- `docs/step27_w_stage1_robustness_improvement_protocol.md`

## Next Action

Review the evidence report against historical
documentation, then update PROJECT_STATUS.md
and complete the Step 27.12-11X Git checkpoint.
