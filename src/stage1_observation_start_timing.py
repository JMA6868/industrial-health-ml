"""Experimental observation-start sensitivity analysis."""

from src.rms_distribution_analysis import get_recording_rms_values
from src.stage1_sequential_alarm import (
    NORMAL_EVAL_IDS,
    FAULT_IDS,
    PERSISTENCE_VALUES,
    SAMPLE_RATE_HZ,
    WINDOW_SIZE,
    WINDOW_STEP,
    evaluate_sequential_alarm,
)

OBSERVATION_START_INDICES = (0, 10, 50, 100)


def evaluate_observation_start(rms_values, start_index, k):
    """Evaluate a fresh alarm counter from a selected window."""
    if not isinstance(start_index, int) or isinstance(start_index, bool):
        raise ValueError("start_index must be an integer")
    if start_index < 0 or start_index >= len(rms_values):
        raise ValueError("start_index must be within the RMS sequence")

    result = evaluate_sequential_alarm(rms_values[start_index:], k)

    relative_index = result["first_alarm_window_index"]

    absolute_index = (
        start_index + relative_index
        if relative_index is not None
        else None
    )

    return {
        "start_index": start_index,
        "k": k,
        "alarm": result["alarm"],
        "first_alarm_relative_window_index": relative_index,
        "first_alarm_absolute_window_index": absolute_index,
        "first_alarm_elapsed_time_s": result["first_alarm_time_s"],
    }


def run_observation_start_analysis():
    """Evaluate selected observation starts for CWRU recordings."""
    results = []

    for recording_id in (*NORMAL_EVAL_IDS, *FAULT_IDS):
        rms_values = get_recording_rms_values(recording_id)

        for start_index in OBSERVATION_START_INDICES:
            if start_index >= len(rms_values):
                raise ValueError(
                    f"Recording {recording_id} is too short "
                    f"for start index {start_index}"
                )

            for k in PERSISTENCE_VALUES:
                result = evaluate_observation_start(
                    rms_values, start_index, k
                )

                result["recording_id"] = recording_id
                result["label"] = (
                    "normal"
                    if recording_id in NORMAL_EVAL_IDS
                    else "fault"
                )

                results.append(result)

    return results
