# Step 27.12-11X — Claim-to-Evidence Matrix

## Purpose

Define accurate, presentation-safe claims for
IndustrialSense AI Stage 1 research.

Evidence categories A-D describe evidence types,
not a ranking of scientific strength.

## Evidence Categories

| Category | Evidence | Scope |
|---|---|---|
| A | Software verification | Tested implementation behavior |
| B | Historical holdout | Original frozen evaluation protocols |
| C | Descriptive evaluation | Previously evaluated CWRU recordings |
| D | Exploratory robustness | Simulations and candidate strategies |

## Claim-to-Evidence Mapping

| Claim | Category | Status | Qualification |
|---|---|---|---|
| Automated regression suite passes 326 tests | A | Supported | Software correctness within tested cases |
| Step 24 RMS threshold 0.18 achieved perfect holdout window metrics | B | Historically supported | Two recordings, 1011 overlapping windows; threshold originated in earlier exploration |
| Step 26 Logistic Regression achieved perfect holdout window metrics | B | Historically supported with qualification | Recordings 100 and 108 were already evaluated in Step 24 |
| Frozen RMS detector identified 45/45 evaluated Fault recordings | C | Supported descriptively | Not an untouched independent holdout |
| Frozen RMS detector raised no alarms on two evaluated Normal recordings | C | Supported descriptively | Very limited Normal sample |
| Simulated Fault attenuation reduced RMS detection coverage | D | Supported | Synthetic amplitude scaling |
| RMS+CF recovered some attenuated Fault recordings | D | Supported exploratorily | Also introduced a Normal alarm |
| Increasing online persistence reduced observed Normal alarms | D | Supported exploratorily | May miss weak or short events |
| Model generalizes to independent physical bearings | None | Not established | Bearing independence unverified |
| Model is production-ready for industrial deployment | None | Not established | Field validation unavailable |
| Measured true fault-onset detection latency | None | Not established | No fault-onset timestamps |
| Proven optimal CF threshold or persistence K | None | Not established | No independent selection/validation |

## Presentation-Safe Statements

### Software

IndustrialSense AI includes a reproducible CWRU
signal-processing and anomaly-detection workflow
with 326 passing automated regression tests.

### Historical Evaluation

Step 24 evaluated an RMS threshold classifier
(threshold 0.18) on recordings 100 and 108.

Step 26 evaluated a frozen Logistic Regression
configuration on those same, previously exposed
holdout recordings.

Both reported perfect window-level classification
under their respective historical protocols.

The later harmonized Stage 1 RMS detector uses
a distinct P99 threshold of 0.07467624803042527.

These results do not establish independent physical
bearing or cross-equipment generalization.

### Current Stage 1 RMS Baseline

The frozen harmonized RMS detector identified
45 of 45 previously evaluated CWRU Fault recordings
and raised no recording-level alarms on two
previously evaluated Normal recordings.

These are descriptive results from reused data.

### Robustness Research

Controlled amplitude-scaling and online-alarm
experiments exposed trade-offs involving Normal
false alarms, attenuated Fault detection,
and alarm persistence.

RMS + Crest Factor showed complementary information
in exploratory tests but was not adopted as the
validated replacement for the frozen baseline.

## Statements to Avoid

- IndustrialSense AI achieves 100% real-world accuracy.
- The system generalizes to previously unseen bearings.
- All 326 passing tests prove fault-detection accuracy.
- Step 24 and Step 26 represent independent test datasets.
- Simulated amplitude attenuation represents measured
  physical fault progression.
- Observation-start time equals true fault-detection latency.
- RMS+CF or K=5 is independently validated as optimal.
- A production deployment is ready without field testing.

## Remaining Evidence Gaps

1. Independently identified physical bearing units.
2. More independent Normal recordings per operating condition.
3. Acquisition and sensor calibration comparability.
4. Untouched evaluation data for new model variants.
5. Measured transient interference and operating shifts.
6. Fault-onset timestamps for detection-latency analysis.
7. External operational validation before deployment claims.

## Next Action

Review this matrix against historical reports
and incorporate its qualified statements into
the final evaluation readiness assessment.
