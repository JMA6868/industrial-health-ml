"""Fault attenuation stress test for frozen Stage 1."""

from src.rms_distribution_analysis import get_recording_rms_values
from src.stage1_normal_amplitude_stress import evaluate_scaled_rms

FAULT_IDS = (
    *range(105, 109),
    *range(118, 122),
    *range(130, 134),
    144, 156, 169, 185, 197,
    *range(209, 213),
    *range(222, 226),
    *range(234, 238),
    *range(246, 250),
    *range(258, 262),
    *range(3001, 3009),
)

ATTENUATION_SCALES = (1.00, 0.75, 0.50, 0.25)


def evaluate_fault_attenuation(rms_values, scale):
    """Evaluate one Fault recording under amplitude attenuation."""
    result = evaluate_scaled_rms(rms_values, scale)

    return {
        "scale": result["scale"],
        "total_windows": result["total_windows"],
        "anomalous_windows": result["anomalous_windows"],
        "anomaly_fraction": result["anomaly_fraction"],
        "detected": result["false_alarm"],
    }


def run_fault_attenuation_stress():
    """Evaluate fixed attenuation scales on all 45 Fault recordings."""
    assert len(FAULT_IDS) == 45
    assert len(set(FAULT_IDS)) == 45

    results = []

    for recording_id in FAULT_IDS:
        rms_values = get_recording_rms_values(recording_id)

        for scale in ATTENUATION_SCALES:
            result = evaluate_fault_attenuation(rms_values, scale)
            result["recording_id"] = recording_id
            results.append(result)

    return results
