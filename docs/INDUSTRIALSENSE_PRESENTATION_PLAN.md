# IndustrialSense AI — Presentation Planning & Tracking

## 1. Purpose

This document is a living plan for presentations to be created
after completion of the IndustrialSense AI project.

It tracks presentation ideas, technical findings, engineering
lessons learned, visual materials, and supporting evidence.

The document should be updated throughout project development
whenever new presentation-worthy ideas emerge.

## 2. Presentation Versions

### 2.1 High-Level Presentation

**Target Audience**
- Hiring managers
- Engineering management
- Nontechnical stakeholders

**Primary Objective**

Communicate the industrial problem, proposed solution,
project accomplishments, and potential engineering value.

**Planned Topics**
- Industrial equipment health-monitoring challenge
- Project vision and objectives
- High-level AI system architecture
- Dataset and application scenario
- Key results and demonstrations
- Engineering value and future opportunities

**Technical Depth:** Low

### 2.2 Middle-Level Presentation

**Target Audience**
- ML engineers
- Research engineers
- Technical interviewers
- Engineering team members

**Primary Objective**

Demonstrate practical ML engineering capability,
research methodology, engineering judgment, and
the ability to critically evaluate experimental results.

**Planned Topics**
- Problem definition and scope
- System architecture and development workflow
- Dataset selection and acquisition background
- Signal preprocessing and feature engineering
- Stage 1 anomaly detection approach
- Baseline modeling and evaluation design
- Experimental results and robustness analysis
- Technical challenges and engineering decisions
- Lessons learned
- Limitations and potential improvements
- Demonstration and future roadmap

**Technical Depth:** Medium

**Required Content**

LL01 — Understand the Dataset Before Modeling

Dedicate at least one slide to this lesson learned,
including:
1. Initial approach
2. What was overlooked
3. How the issue was discovered
4. Impact on interpreting ML results
5. Improved methodology for future projects

### 2.3 Detailed Technical Presentation

**Target Audience**
- ML specialists
- Research collaborators
- Technical reviewers
- Code reviewers

**Primary Objective**

Provide a detailed, reproducible explanation of
the system architecture, algorithms, implementation,
experimental design, and research limitations.

**Planned Topics**
- Detailed architecture and repository structure
- CWRU dataset metadata and experimental background
- Data-loading and signal-validation implementation
- Signal resampling and frequency-band analysis
- Sliding-window feature extraction
- RMS threshold calibration
- Recording-level anomaly aggregation
- Dataset splitting and leakage prevention
- Model evaluation methodology
- RMS distribution and separation investigation
- Amplitude sensitivity analysis
- Preprocessing-confound investigation
- Fault type, diameter, and load comparisons
- Automated tests and reproducibility
- Source code and design tradeoffs
- Research limitations and future development

**Technical Depth:** High

## 3. Presentation Content Tracker

Status definitions:
- IDEA: Candidate content
- COLLECTING: Supporting evidence being gathered
- READY: Evidence and material prepared
- DRAFTED: Added to a presentation
- FINAL: Reviewed and finalized

| ID | Topic | High | Middle | Detailed | Status |
|---|---|---|---|---|---|
| P01 | Project problem and motivation | Yes | Yes | Yes | IDEA |
| P02 | Overall system architecture | Yes | Yes | Yes | IDEA |
| P03 | CWRU dataset overview | Brief | Yes | Yes | COLLECTING |
| P04 | Stage 1 RMS baseline | Summary | Yes | Yes | COLLECTING |
| P05 | Evaluation methodology and leakage | Brief | Yes | Yes | COLLECTING |
| P06 | RMS separation and sensitivity | Optional | Yes | Yes | COLLECTING |
| P07 | Sampling-rate and filtering investigation | No | Yes | Yes | COLLECTING |
| P08 | LL01 — Dataset provenance lesson learned | Optional | REQUIRED | Yes | COLLECTING |
| P09 | Automated testing and reproducibility | No | Summary | Yes | COLLECTING |
| P10 | Model comparison and future AI development | Yes | Yes | Yes | IDEA |
| P11 | Interactive demonstration | Yes | Yes | Yes | IDEA |
| P12 | Project limitations and future work | Yes | Yes | Yes | IDEA |

## 4. Engineering Lessons Learned Tracker

| ID | Lesson Learned | Priority | Middle PPT | Status |
|---|---|---|---|---|
| LL01 | Understand the Dataset Before Modeling | High | Required | Documented |

Lesson learned reference:

`docs/lessons_learned/LL01_dataset_provenance.md`

Future lessons learned should be added to this table
as they are identified and documented.

## 5. Research Evidence and Sources

### Stage 1 RMS Evaluation

- `docs/step27_expanded_stage1_results.md`
- `docs/step27_additional_fault_results.md`
- `docs/step27_additional_fault_results.csv`

### RMS Separation and Robustness

- `docs/step27_rms_separation_investigation.md`

### Data Acquisition and Preprocessing

- `docs/step27_acquisition_preprocessing_investigation.md`
- `docs/step27_official_acquisition_metadata_audit.md`

### Lessons Learned

- `docs/lessons_learned/LL01_dataset_provenance.md`

## 6. Visual Materials Tracker

Potential presentation visuals:

| ID | Visual | Purpose | Status |
|---|---|---|---|
| V01 | Overall IndustrialSense AI architecture | Explain system design | IDEA |
| V02 | CWRU data-processing pipeline | Explain preprocessing | IDEA |
| V03 | Normal vs Fault RMS distribution | Explain baseline behavior | IDEA |
| V04 | Recording-level detection flowchart | Explain decision logic | IDEA |
| V05 | RMS threshold sensitivity chart | Explain robustness | IDEA |
| V06 | Sampling-rate and frequency-band comparison | Explain preprocessing effects | IDEA |
| V07 | Dataset provenance audit workflow | Explain LL01 | IDEA |
| V08 | Model evaluation comparison | Compare approaches | IDEA |
| V09 | Interactive demo screenshots | Demonstrate working system | IDEA |

All final visuals should be traceable to actual
project results or verified project architecture.

## 7. Presentation Design Principles

1. Use the same technical facts across all three versions.
2. Adjust depth and explanation for the target audience.
3. Distinguish observed results from generalization claims.
4. Avoid inflated performance statements.
5. Identify assumptions and experimental limitations.
6. Use real project evidence rather than invented examples.
7. Show engineering decisions and their rationale.
8. Highlight learning, investigation, and iteration.
9. Maintain consistent terminology and visual design.
10. Keep all three versions synchronized as the project evolves.

## 8. Future Presentation Deliverables

Planned final outputs:

- High-Level PPT (.pptx)
- Middle-Level PPT (.pptx)
- Detailed Technical PPT (.pptx)

Optional supporting materials:

- Demo video
- Architecture diagrams
- Research figures
- Technical appendix
- GitHub repository walkthrough
- Speaker notes

Presentation development will begin when the project
has sufficient completed results and demonstration material.

## 9. New Ideas and Change Log

Add new ideas here whenever they arise during development.

Use this format:

### IDEA-XXX — Short Title

**Date:** YYYY-MM-DD

**Idea:**

Description of the proposed presentation content.

**Target Version(s):**

High / Middle / Detailed

**Supporting Evidence:**

Relevant project files, experiments, or code.

**Status:** IDEA

---

### IDEA-001 — Highlight Dataset Provenance Lesson Learned

**Date:** 2026-11-09

**Idea:**

Use the late discovery of CWRU acquisition metadata
differences as a concrete example of an engineering
lesson learned.

Show how the project initially focused on data-format
validation but later identified important differences
in bearing manufacturer, fault depth, and preprocessing.

Explain why dataset provenance should be reviewed
before model development and performance evaluation.

**Target Version(s):**

Middle (Required), Detailed

**Supporting Evidence:**

- `docs/lessons_learned/LL01_dataset_provenance.md`
- `docs/step27_official_acquisition_metadata_audit.md`
- `docs/step27_acquisition_preprocessing_investigation.md`

**Status:** COLLECTING

---

## 10. Maintenance Rules

- Treat this file as a living project document.
- Add ideas as they arise; do not wait until project completion.
- Preserve historical decisions and lessons learned.
- Update content-tracker statuses as evidence becomes ready.
- Reference committed research files whenever possible.
- Do not mark unverified results as final.
- Review this plan before creating the three PPT versions.
- Middle-Level PPT must include LL01.
