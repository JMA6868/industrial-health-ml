# Step 27.12-11T — Official CWRU Acquisition Metadata Audit

## Status

Official documentation review in progress.

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

The 0.028-inch subset differs in diameter, defect depth,
and manufacturer. These factors must not be treated as independent.

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
