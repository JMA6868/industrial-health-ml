"""Normal-recording threshold margin diagnostics."""

import math

import numpy as np

from src.stage1_normal_amplitude_stress import FROZEN_THRESHOLD


def analyze_normal_threshold_margin(
    rms_values,
    threshold=FROZEN_THRESHOLD,
    recording_fraction=0.05,
):
    """Analyze frozen-threshold sensitivity under uniform scaling."""
    values = np.asarray(rms_values, dtype=float)

    if values.ndim != 1 or values.size == 0:
        raise ValueError("RMS values must be a nonempty 1D array")

    if not np.isfinite(values).all() or np.any(values < 0):
        raise ValueError("RMS values must be finite and nonnegative")

    if not np.isfinite(threshold) or threshold <= 0:
        raise ValueError("Threshold must be finite and positive")

    if (
        not np.isfinite(recording_fraction)
        or not 0 <= recording_fraction < 1
    ):
        raise ValueError("Recording fraction must be in [0, 1)")

    n = len(values)
    required = math.floor(recording_fraction * n) + 1
    boundary_rms = np.sort(values)[-required]

    critical_scale = (
        float(threshold / boundary_rms)
        if boundary_rms > 0
        else math.inf
    )

    anomalous = int(np.count_nonzero(values > threshold))

    return {
        "total_windows": n,
        "required_anomalous_windows": required,
        "anomalous_windows": anomalous,
        "recording_alarm": anomalous >= required,
        "mean_rms": float(np.mean(values)),
        "max_margin": float(threshold - np.max(values)),
        "p95_margin": float(
            threshold - np.percentile(values, 95)
        ),
        "p99_margin": float(
            threshold - np.percentile(values, 99)
        ),
        "boundary_rms": float(boundary_rms),
        "critical_scale": critical_scale,
    }
