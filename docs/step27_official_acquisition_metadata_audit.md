# Step 27.12-11T — Official CWRU Acquisition Metadata Audit

## Status

Completed — published CWRU acquisition metadata reviewed. Unverified acquisition details remain documented.

## Verified Official Information

- Test stand: 2 HP motor, torque transducer/encoder, dynamometer.
- Fault creation: electro-discharge machining (EDM).
- Sensors: accelerometers mounted with magnetic bases.
- Sensor positions: drive-end and fan-end motor housing.
- Data acquisition: 16-channel DAT recorder.
- Data format: MATLAB MAT files.
- Available drive-end fault datasets: 12 kHz and 48 kHz.

## Drive-End Fault Specifications

| Diameter (in) | Fault Location | Depth (in) | Manufacturer |
|---|---|---|---|
| 0.007 | Inner race / Outer race / Ball | 0.011 | SKF |
| 0.014 | Inner race / Outer race / Ball | 0.011 | SKF |
| 0.021 | Inner race / Outer race / Ball | 0.011 | SKF |
| 0.028 | Inner race | 0.050 | NTN |
| 0.028 | Ball | 0.150 | NTN |
| 0.040 | Outer race | 0.050 | NTN |

The 0.040-inch outer-race specification is listed in the
official fault specifications, but it is not listed in the
published 12 kHz Drive-End data table.

The 0.028-inch subset differs in diameter, defect depth,
and manufacturer. These factors must not be treated as independent.

## Outer-Race Fault Orientation

Official CWRU documentation describes outer-race fault
positions at 3, 6, and 12 o'clock relative to the load zone.

Fault orientation may influence the measured vibration
response and RMS amplitude.

The 19 evaluated outer-race recordings have been checked
against the official CWRU 12 kHz Drive-End data table.

Therefore, RMS differences must not be attributed to
fault diameter or severity alone without considering
fault orientation and other acquisition conditions.

## Evaluated Outer-Race Recording Coverage

Project records identify the following evaluated recordings:

| Orientation | Recording IDs | Count |
|---|---|---:|
| 6:00 | 130-133, 197, 234-237 | 9 |
| 3:00 | 144, 246-249 | 5 |
| 12:00 | 156, 258-261 | 5 |
| Total | | 19 |

All 19 outer-race recordings were detected by the frozen
Stage 1 RMS baseline in the project's descriptive evaluation.

These classifications are consistent across existing project
documents and the official CWRU 12 kHz Drive-End data table.
This verifies published recording metadata, not physical-bearing
independence or acquisition-gain equivalence.

## Unverified Information

- Exact sensor calibration and measurement units for each recording.
- Whether acquisition gain was identical across recordings.
- Whether all recordings used identical sensor hardware.
- Independent physical-bearing identities.
- Whether observed RMS differences are caused by specific
  acquisition settings.

## Implications

The previously observed large RMS detection margins for
0.028-inch faults cannot be attributed to diameter alone.

Official documentation establishes potential confounding
variables but does not establish their causal effects.

## Official Sources

- https://engineering.case.edu/bearingdatacenter/apparatus-and-procedures
- https://engineering.case.edu/bearingdatacenter/fault-specifications
- https://engineering.case.edu/bearingdatacenter/download-data-file
- https://engineering.case.edu/bearingdatacenter/normal-baseline-data
- https://engineering.case.edu/bearingdatacenter/12k-drive-end-bearing-fault-data

## Project Constraints

Preserve the frozen Stage 1 RMS baseline.
Do not infer missing acquisition metadata.
Do not claim independent cross-bearing generalization.
