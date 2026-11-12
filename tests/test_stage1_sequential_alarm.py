"""Tests for experimental Stage 1 sequential alarms."""

import numpy as np
import pytest

from src.stage1_sequential_alarm import evaluate_sequential_alarm


@pytest.mark.parametrize(
    "k, expected_index, expected_time",
    [(1, 0, 0.10), (3, 2, 0.20), (5, 4, 0.30)],
)
def test_consecutive_alarm_timing(k, expected_index, expected_time):
    result = evaluate_sequential_alarm([0.10] * 5, k)

    assert result["alarm"] is True
    assert result["first_alarm_window_index"] == expected_index
    assert result["first_alarm_time_s"] == pytest.approx(expected_time)


def test_interrupted_sequence_resets_counter():
    result = evaluate_sequential_alarm(
        [0.10, 0.10, 0.01, 0.10, 0.10, 0.10], 3
    )

    assert result["alarm"] is True
    assert result["first_alarm_window_index"] == 5
    assert result["first_alarm_time_s"] == pytest.approx(0.35)


def test_no_alarm_when_consecutive_count_insufficient():
    result = evaluate_sequential_alarm([0.10, 0.01, 0.10], 2)

    assert result["alarm"] is False
    assert result["first_alarm_window_index"] is None
    assert result["first_alarm_time_s"] is None


def test_strict_rms_threshold_boundary():
    threshold = 0.07467624803042527
    result = evaluate_sequential_alarm([threshold], 1)

    assert result["alarm"] is False


def test_alarm_when_rms_exceeds_threshold():
    threshold = 0.07467624803042527
    result = evaluate_sequential_alarm(
        [np.nextafter(threshold, np.inf)], 1
    )

    assert result["alarm"] is True


@pytest.mark.parametrize(
    "values, k",
    [
        ([], 1),
        ([np.nan], 1),
        ([np.inf], 1),
        ([0.10], 0),
        ([0.10], -1),
        ([0.10], 1.5),
        ([0.10], True),
    ],
)
def test_invalid_inputs(values, k):
    with pytest.raises(ValueError):
        evaluate_sequential_alarm(values, k)
