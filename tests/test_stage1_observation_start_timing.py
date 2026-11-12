"""Tests for Stage 1 observation-start timing analysis."""

import numpy as np
import pytest

from src.stage1_observation_start_timing import (
    evaluate_observation_start,
)


def test_alarm_from_new_observation_start():
    values = [0.01] * 10 + [0.10] * 5

    result = evaluate_observation_start(values, 10, 3)

    assert result["alarm"] is True
    assert result["first_alarm_relative_window_index"] == 2
    assert result["first_alarm_absolute_window_index"] == 12
    assert result["first_alarm_elapsed_time_s"] == pytest.approx(0.20)


def test_counter_resets_at_observation_start():
    values = [0.10, 0.10, 0.01, 0.01]

    result = evaluate_observation_start(values, 1, 2)

    assert result["alarm"] is False
    assert result["first_alarm_relative_window_index"] is None
    assert result["first_alarm_absolute_window_index"] is None
    assert result["first_alarm_elapsed_time_s"] is None


def test_alarm_after_interrupted_sequence():
    values = [0.01] * 5 + [
        0.10, 0.10, 0.01, 0.10, 0.10, 0.10
    ]

    result = evaluate_observation_start(values, 5, 3)

    assert result["alarm"] is True
    assert result["first_alarm_relative_window_index"] == 5
    assert result["first_alarm_absolute_window_index"] == 10
    assert result["first_alarm_elapsed_time_s"] == pytest.approx(0.35)


@pytest.mark.parametrize(
    "k, expected_relative, expected_time",
    [(1, 0, 0.10), (3, 2, 0.20), (5, 4, 0.30)],
)
def test_persistence_timing(k, expected_relative, expected_time):
    values = [0.01] * 10 + [0.10] * 5

    result = evaluate_observation_start(values, 10, k)

    assert result["first_alarm_relative_window_index"] == expected_relative
    assert result["first_alarm_absolute_window_index"] == (
        10 + expected_relative
    )
    assert result["first_alarm_elapsed_time_s"] == pytest.approx(
        expected_time
    )


def test_no_alarm_on_normal_windows():
    result = evaluate_observation_start([0.01] * 20, 10, 3)

    assert result["alarm"] is False
    assert result["first_alarm_elapsed_time_s"] is None


@pytest.mark.parametrize("start_index", [-1, 3, 1.5, True])
def test_invalid_start_indices(start_index):
    with pytest.raises(ValueError):
        evaluate_observation_start([0.10, 0.10, 0.10], start_index, 1)


def test_empty_sequence_rejected():
    with pytest.raises(ValueError):
        evaluate_observation_start([], 0, 1)


def test_invalid_rms_values_rejected():
    with pytest.raises(ValueError):
        evaluate_observation_start(
            np.array([0.10, np.nan, 0.10]), 0, 2
        )


def test_invalid_persistence_rejected():
    with pytest.raises(ValueError):
        evaluate_observation_start([0.10] * 5, 0, 0)
