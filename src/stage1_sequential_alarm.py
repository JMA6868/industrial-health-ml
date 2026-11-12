"""Experimental sequential alarm analysis for Stage 1."""

import numpy as np

from src.rms_distribution_analysis import get_recording_rms_values
from src.stage1_fault_attenuation_stress import FAULT_IDS
from src.stage1_normal_amplitude_stress import FROZEN_THRESHOLD

NORMAL_EVAL_IDS = (99, 100)
PERSISTENCE_VALUES = (1, 3, 5)

SAMPLE_RATE_HZ = 12000
WINDOW_SIZE = 1200
WINDOW_STEP = 600


def evaluate_sequential_alarm(rms_values, k, threshold=FROZEN_THRESHOLD):
    """Find first K-consecutive-anomaly alarm."""
    values = np.asarray(rms_values, dtype=float)

    if values.ndim != 1 or values.size == 0:
        raise ValueError("RMS values must be a nonempty 1D array")
    if not np.isfinite(values).all():
        raise ValueError("RMS values must be finite")
    if not isinstance(k, int) or isinstance(k, bool) or k <= 0:
        raise ValueError("k must be a positive integer")
    if not np.isfinite(threshold) or threshold < 0:
        raise ValueError("Threshold must be finite and nonnegative")

    flags = values > threshold
    consecutive = 0

    for index, anomalous in enumerate(flags):
        consecutive = consecutive + 1 if anomalous else 0

        if consecutive >= k:
            end_sample = index * WINDOW_STEP + WINDOW_SIZE
            return {
                "alarm": True,
                "first_alarm_window_index": index,
                "first_alarm_time_s": end_sample / SAMPLE_RATE_HZ,
            }

    return {
        "alarm": False,
        "first_alarm_window_index": None,
        "first_alarm_time_s": None,
    }


def run_sequential_alarm_analysis():
    """Evaluate original Normal and Fault RMS sequences."""
    results = []

    for recording_id in (*NORMAL_EVAL_IDS, *FAULT_IDS):
        rms_values = get_recording_rms_values(recording_id)

        for k in PERSISTENCE_VALUES:
            result = evaluate_sequential_alarm(rms_values, k)
            result["recording_id"] = recording_id
            result["label"] = (
                "normal" if recording_id in NORMAL_EVAL_IDS else "fault"
            )
            result["k"] = k
            results.append(result)

    return results
