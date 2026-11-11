"""Normal amplitude stress test for frozen Stage 1."""

import numpy as np

from src.recording_anomaly_decision import classify_recording
from src.rms_distribution_analysis import get_recording_rms_values


FROZEN_THRESHOLD = 0.07467624803042527
NORMAL_EVAL_IDS = (99, 100)
AMPLITUDE_SCALES = (1.00, 1.05, 1.10, 1.20, 1.50)


def evaluate_scaled_rms(rms_values, scale, threshold=FROZEN_THRESHOLD):
    """Evaluate a scaled RMS sequence without threshold tuning."""
    values = np.asarray(rms_values, dtype=float)

    if values.ndim != 1 or values.size == 0:
        raise ValueError("RMS values must be a nonempty 1D array")
    if not np.isfinite(values).all():
        raise ValueError("RMS values must be finite")
    if not np.isfinite(scale) or scale <= 0:
        raise ValueError("Scale must be positive and finite")

    anomalous = int(np.count_nonzero(values * scale > threshold))
    total = int(values.size)

    return {
        "scale": float(scale),
        "total_windows": total,
        "anomalous_windows": anomalous,
        "anomaly_fraction": anomalous / total,
        "false_alarm": classify_recording(anomalous, total),
    }


def run_normal_amplitude_stress():
    """Evaluate fixed amplitude scales on Normal recordings 99/100."""
    results = []

    for recording_id in NORMAL_EVAL_IDS:
        rms_values = get_recording_rms_values(recording_id)

        for scale in AMPLITUDE_SCALES:
            result = evaluate_scaled_rms(rms_values, scale)
            result["recording_id"] = recording_id
            results.append(result)

    return results
