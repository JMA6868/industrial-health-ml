"""Tests for normal threshold margin diagnostics."""

import math

import numpy as np
import pytest

from src.stage1_normal_threshold_margin import (
    analyze_normal_threshold_margin,
)


def test_required_anomalies_for_100_windows():
    values = [0.01] * 94 + [0.10] * 6
    result = analyze_normal_threshold_margin(values)

    assert result["required_anomalous_windows"] == 6
    assert result["anomalous_windows"] == 6
    assert result["recording_alarm"] is True


def test_five_percent_exactly_does_not_alarm():
    values = [0.01] * 95 + [0.10] * 5
    result = analyze_normal_threshold_margin(values)

    assert result["anomalous_windows"] == 5
    assert result["recording_alarm"] is False


def test_critical_scale_boundary():
    values = np.array([0.04] * 94 + [0.06] * 6)
    result = analyze_normal_threshold_margin(
        values, threshold=0.075
    )

    assert result["critical_scale"] == pytest.approx(1.25)
    assert result["required_anomalous_windows"] == 6

    below = analyze_normal_threshold_margin(
        values * 1.249, threshold=0.075
    )
    above = analyze_normal_threshold_margin(
        values * 1.251, threshold=0.075
    )

    assert below["recording_alarm"] is False
    assert above["recording_alarm"] is True


def test_single_window_requires_one_anomaly():
    result = analyze_normal_threshold_margin(
        [0.10], threshold=0.075
    )

    assert result["required_anomalous_windows"] == 1
    assert result["recording_alarm"] is True


def test_all_zero_rms_values():
    result = analyze_normal_threshold_margin(
        [0.0] * 100
    )

    assert result["recording_alarm"] is False
    assert math.isinf(result["critical_scale"])


def test_original_recording_already_alarms():
    result = analyze_normal_threshold_margin(
        [0.10] * 100, threshold=0.075
    )

    assert result["recording_alarm"] is True
    assert result["critical_scale"] == pytest.approx(0.75)


def test_margin_statistics():
    result = analyze_normal_threshold_margin(
        [0.02, 0.04, 0.06, 0.08],
        threshold=0.075,
    )

    assert result["mean_rms"] == pytest.approx(0.05)
    assert result["max_margin"] == pytest.approx(-0.005)
    assert result["p95_margin"] > result["max_margin"]


@pytest.mark.parametrize(
    "values",
    [
        [],
        [-0.01, 0.02],
        [np.nan],
        [np.inf],
        [[0.01, 0.02]],
    ],
)
def test_invalid_rms_values(values):
    with pytest.raises(ValueError):
        analyze_normal_threshold_margin(values)


@pytest.mark.parametrize(
    "threshold",
    [0, -0.1, np.nan, np.inf],
)
def test_invalid_threshold(threshold):
    with pytest.raises(ValueError):
        analyze_normal_threshold_margin(
            [0.01], threshold=threshold
        )


@pytest.mark.parametrize(
    "fraction",
    [-0.1, 1.0, np.nan, np.inf],
)
def test_invalid_recording_fraction(fraction):
    with pytest.raises(ValueError):
        analyze_normal_threshold_margin(
            [0.01], recording_fraction=fraction
        )
