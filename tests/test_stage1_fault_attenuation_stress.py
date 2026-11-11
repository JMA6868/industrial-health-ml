"""Tests for Stage 1 fault attenuation stress."""

import numpy as np
import pytest

from src.stage1_fault_attenuation_stress import (
    evaluate_fault_attenuation,
    FAULT_IDS,
    ATTENUATION_SCALES,
)


def test_fault_detected_without_attenuation():
    values = np.full(100, 0.10)
    result = evaluate_fault_attenuation(values, 1.0)

    assert result["anomalous_windows"] == 100
    assert result["detected"] is True


def test_fault_missed_after_attenuation():
    values = np.full(100, 0.10)
    result = evaluate_fault_attenuation(values, 0.5)

    assert result["anomalous_windows"] == 0
    assert result["detected"] is False


def test_exact_five_percent_boundary():
    values = np.array([0.10] * 5 + [0.04] * 95)
    result = evaluate_fault_attenuation(values, 1.0)

    assert result["anomaly_fraction"] == 0.05
    assert result["detected"] is False


def test_above_five_percent_boundary():
    values = np.array([0.10] * 6 + [0.04] * 94)
    result = evaluate_fault_attenuation(values, 1.0)

    assert result["anomaly_fraction"] == 0.06
    assert result["detected"] is True


@pytest.mark.parametrize("scale", [0.0, -0.5, np.nan, np.inf])
def test_invalid_scales(scale):
    with pytest.raises(ValueError):
        evaluate_fault_attenuation([0.10], scale)


def test_fault_recording_inventory():
    assert len(FAULT_IDS) == 45
    assert len(set(FAULT_IDS)) == 45
    assert ATTENUATION_SCALES == (1.0, 0.75, 0.5, 0.25)
