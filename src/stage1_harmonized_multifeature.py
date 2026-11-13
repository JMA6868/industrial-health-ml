"""Harmonized CWRU RMS and Crest Factor feature extraction."""

from pathlib import Path

import numpy as np

from src.cwru_preprocessing import load_harmonized_cwru_signal
from src.feature_extraction import extract_window_features
from src.exploratory_signal_features import calculate_crest_factor
from src.harmonized_stage1_evaluation import WINDOW_SIZE, STEP

NORMAL_IDS = (97, 98, 99, 100)


def extract_harmonized_multifeatures(signal):
    """Extract RMS and Crest Factor from identical signal windows."""
    values = np.asarray(signal, dtype=float)

    if values.ndim != 1 or values.size < WINDOW_SIZE:
        raise ValueError("Signal must be 1D and at least one window long")

    if not np.isfinite(values).all():
        raise ValueError("Signal must contain only finite values")

    features = extract_window_features(
        values,
        window_size=WINDOW_SIZE,
        step=STEP,
    )

    results = []

    for feature in features:
        start = feature["start_index"]
        window = values[start:start + WINDOW_SIZE]

        results.append({
            "start_index": start,
            "end_index": feature["end_index"],
            "rms": feature["rms"],
            "crest_factor": calculate_crest_factor(window),
        })

    return results


def get_harmonized_multifeatures(recording_id):
    """Load an official CWRU recording with verified sample rate."""
    if isinstance(recording_id, bool) or not isinstance(recording_id, int):
        raise ValueError("recording_id must be an integer")

    source_rate = 48000 if recording_id in NORMAL_IDS else 12000

    signal = load_harmonized_cwru_signal(
        Path(f"data/raw/cwru/{recording_id}.mat"),
        source_rate_hz=source_rate,
    )

    return extract_harmonized_multifeatures(signal)
