# LL01 — Understand the Dataset Before Modeling

## Status

Confirmed engineering lesson learned.

## Presentation Priority

- High-Level PPT: Optional brief mention.
- Middle-Level PPT: MUST INCLUDE.
- Detailed PPT: Include supporting metadata and experiments.

## What Happened

During the early stages of IndustrialSense AI, we validated:

- Data file formats and signal structures
- Data loading and signal extraction
- Sampling rates and preprocessing
- Feature extraction
- Dataset splitting and evaluation

However, we did not systematically investigate the
complete experimental background and acquisition metadata
before developing and evaluating the RMS baseline.

This gap was identified later, after extensive Stage 1
experiments had already been completed.

## What We Discovered

The official CWRU documentation indicates that the
0.028-inch fault subset differs from other fault groups
in several characteristics:

- Fault diameter
- Fault depth
- Bearing manufacturer

Our previous experiments showed particularly large
RMS detection margins for these recordings.

However, the observed differences cannot be attributed
to fault diameter alone.

We also discovered that sampling-rate harmonization
and filtering can materially change RMS distributions
and fixed-threshold classification results.

## Why This Matters

Data validation is not limited to checking whether
files are readable, complete, and correctly labeled.

It must also examine:

- Data provenance
- Experimental setup
- Sensor type, position, and calibration
- Data acquisition settings and gain
- Sampling rates and measurement bandwidth
- Equipment and specimen differences
- Operating conditions
- Label generation and fault creation methods
- Potential confounding variables
- Physical-unit and specimen independence

A technically correct ML pipeline can produce impressive
results while important dataset-level confounding
factors remain unidentified.

## What We Would Do Differently

Before model development:

1. Read the dataset's original technical documentation.
2. Build a structured acquisition metadata inventory.
3. Identify differences between Normal and Fault groups.
4. Record missing metadata explicitly.
5. Identify potential confounding variables.
6. Evaluate whether the proposed dataset split supports
   the intended generalization claims.
7. Document assumptions before training models.

## Recommended Project Workflow

Dataset Discovery
    -> Data Provenance and Acquisition Audit
    -> Data Format and Quality Validation
    -> Leakage-Aware Dataset Splitting
    -> Preprocessing and Feature Engineering
    -> Baseline Modeling
    -> Evaluation and Robustness Investigation

## Middle-Level PPT Message

**Lesson Learned: Data Understanding Must Precede Modeling**

We initially focused on technical data validation but
reviewed acquisition metadata too late.

Later investigation revealed differences in bearing
manufacturer, fault depth, and preprocessing sensitivity.

This taught us to treat data provenance and experimental
conditions as first-class ML engineering requirements.

## Supporting Project Evidence

- docs/step27_official_acquisition_metadata_audit.md
- docs/step27_acquisition_preprocessing_investigation.md
- docs/step27_rms_separation_investigation.md

## Future Application

Apply a formal Dataset Provenance & Acquisition Audit
at the start of future machine learning projects.
