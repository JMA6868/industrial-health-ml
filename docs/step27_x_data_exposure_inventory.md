# Step 27.12-11X — CWRU Data Exposure Inventory

## Status

Historical recording-level roles and subsequent
evaluation exposure documented.

## Original Recording-Level Split

| Role | Normal | Fault |
|---|---|---|
| Train | 97, 98 | 105, 106 |
| Validation | 99 | 107 |
| Test | 100 | 108 |

Source: `src/dataset_split.py`.

The original split is recording-disjoint but
physical-bearing independence is not established.

## Current Frozen Stage 1 Calibration

- Normal calibration recordings: 97, 98.
- Sampling rate harmonized to 12000 Hz.
- RMS window length: 1200 samples.
- Window step: 600 samples.
- Threshold: 0.07467624803042527.
- RMS threshold derived from Normal training P99.
- Recording-level rule: anomalous fraction > 0.05.

Source: `src/harmonized_stage1_evaluation.py`.

The early supervised split and current RMS
calibration workflow are not identical.

## Recording Exposure Classification

| Recordings | Original Role | Subsequent Exposure |
|---|---|---|
| 97, 98 | Train / calibration | RMS and CF calibration, descriptive analysis |
| 99 | Validation | Normal evaluation, U1, V1, W2/W3 |
| 100 | Test | Normal evaluation, U1, V1, W2/W3 |
| 105, 106 | Supervised Train | Later Stage 1 Fault evaluations |
| 107 | Supervised Validation | Later Stage 1 Fault evaluations |
| 108 | Supervised Test | Later Stage 1 Fault evaluations |
| Other 41 Fault recordings | Expansion evaluations | U2, U3/U4, W2/W3 explorations |

Historical role labels are preserved.
Subsequent exposure does not retroactively invalidate
a genuinely frozen earlier evaluation, but these
recordings cannot become untouched tests again.

## Available CWRU Recordings

- Total local inventory: 49 recordings.
- Normal: 4 recordings.
- Fault: 45 recordings.
- Every Normal recording has been used or examined.
- All 45 Fault recordings have been evaluated or examined.
- No untouched local recording-level holdout remains
  for later detector selection and final evaluation.

## Historical Holdout Evaluations

### Step 24 — Frozen-Threshold Holdout

- Recording-level Train/Validation/Test separation
  was established before window generation.
- The RMS threshold was frozen before holdout evaluation.
- Holdout recordings: Normal 100 and Fault 108.
- Holdout evaluation: 1,011 overlapping windows.
- Historical metrics: TN=808, FP=0, FN=0, TP=203.
- Window-level classification metrics were 1.0000.

### Step 26 — Frozen-Configuration ML Holdout

- The ML configuration was frozen before final evaluation.
- Final holdout recordings: Normal 100 and Fault 108.
- Historical metrics: TN=808, FP=0, FN=0, TP=203.
- Accuracy, Precision, Recall, and F1 were 1.000.

### Interpretation and Exposure Timeline

These results should be preserved as historical
holdout evaluations under their original protocols.

Step 24 and Step 26 used the same recording-level
holdout IDs and must not be counted as two
independent physical validation datasets.

After these evaluations, the recordings were further
examined during later Stage 1 experiments.

This subsequent exposure does not automatically
invalidate an earlier properly frozen evaluation.

However, the same recordings cannot be reused as
untouched holdouts for later model selection or
newly developed detector variants.

The historical window-level perfect scores do not
establish generalization to independent physical
bearings, unfamiliar equipment, or industrial sites.

## Historical Model and Holdout Distinctions

### Step 24 — RMS Threshold Classifier

- Rule-based RMS threshold classifier.
- Fixed RMS threshold: 0.18.
- Threshold originated in earlier exploratory development.
- Holdout recordings: 100 and 108.
- Holdout confusion matrix: TN=808, FP=0, FN=0, TP=203.
- This was not a newly trained ML classifier.

### Step 26 — Logistic Regression ML Baseline

- StandardScaler and LogisticRegression pipeline.
- Training features: Mean, Std, and RMS.
- Model configuration frozen before final evaluation.
- Holdout recordings: 100 and 108.
- Holdout confusion matrix: TN=808, FP=0, FN=0, TP=203.
- The same holdout recordings had already been
  evaluated during Step 24.

### Relationship to Later Stage 1 Baseline

The later harmonized Stage 1 RMS detector uses
a separate training-derived P99 threshold:

0.07467624803042527

It should not be conflated with the historical
Step 24 threshold of 0.18 or the Step 26 ML model.

### Evidence Qualification

Step 24 provides a historical frozen-threshold
evaluation under its documented protocol.

Step 26 provides a historical frozen-configuration
ML evaluation on previously exposed holdout recordings.

Neither establishes physical-bearing-independent
generalization or current untouched test performance.

The two experiments share test recordings and
must not be counted as independent validation sets.

## Independence Limitations

- Distinct recording IDs do not prove independent bearings.
- Physical-bearing and defect-instance identity is not
  sufficiently established for independent generalization.
- Normal/Fault acquisition and sampling-rate differences
  introduce additional confounding.
- Overlapping windows are correlated observations.
- Repeated perturbations of the same recording are not
  independent physical experiments.

## Permitted Claims

- Original split is disjoint at recording-ID level.
- Software functions have automated regression tests.
- Frozen Stage 1 descriptive results can be reported
  with their actual calibration and exposure history.
- Simulated robustness outcomes can be presented
  as exploratory analyses of specified recordings.

## Claims Not Supported

- New untouched holdout performance for W2/W3.
- Independent physical-bearing generalization.
- General industrial equipment fault-detection accuracy.
- Field false-alarm rates or real fault-onset alarm delay.
- Independent validation based on resplitting
  previously examined recording IDs.

## Next Action

Cross-check historical experiment documentation
against this inventory, then build a claim-to-evidence
matrix and independent evaluation readiness assessment.
