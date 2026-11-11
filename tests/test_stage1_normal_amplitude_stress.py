"""Tests for Stage 1 normal amplitude stress."""

import numpy as np
import pytest

from src.stage1_normal_amplitude_stress import (
    evaluate_scaled_rms,
)


def test_no_false_alarm():
    values = np.full(100, 0.04)

    result = evaluate_scaled_rms(values, 1.0)

    assert result["total_windows"] == 100
    assert result["anomalous_windows"] == 0
    assert result["anomaly_fraction"] == 0.0
    assert result["false_alarm"] is False


def test_amplitude_scaling_triggers_alarm():
    values = np.full(100, 0.04)

    result = evaluate_scaled_rms(values, 2.0)

    assert result["anomalous_windows"] == 100
    assert result["anomaly_fraction"] == 1.0
    assert result["false_alarm"] is True


def test_exactly_five_percent_no_alarm():
    values = np.array([0.08] * 5 + [0.04] * 95)

    result = evaluate_scaled_rms(values, 1.0)

    assert result["anomalous_windows"] == 5
    assert result["false_alarm"] is False


def test_above_five_percent_triggers_alarm():
    values = np.array([0.08] * 6 + [0.04] * 94)

    result = evaluate_scaled_rms(values, 1.0)

    assert result["anomalous_windows"] == 6
    assert result["false_alarm"] is True


@pytest.mark.parametrize(
    "values, scale",
    [
        ([], 1.0),
        ([np.nan], 1.0),
        ([np.inf], 1.0),
        ([0.04], 0.0),
        ([0.04], -1.0),
        ([0.04], np.nan),
    ],
)
def test_invalid_inputs(values, scale):
    with pytest.raises(ValueError):
        evaluate_scaled_rms(values, scale)
