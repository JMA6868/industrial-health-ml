"""Tests for harmonized RMS and Crest Factor extraction."""

import numpy as np
import pytest

from src.stage1_harmonized_multifeature import (
    extract_harmonized_multifeatures,
    WINDOW_SIZE,
    STEP,
)


def test_single_constant_window():
    signal = np.full(WINDOW_SIZE, 2.0)

    results = extract_harmonized_multifeatures(signal)

    assert len(results) == 1
    assert results[0]["start_index"] == 0
    assert results[0]["end_index"] == WINDOW_SIZE - 1
    assert results[0]["rms"] == pytest.approx(2.0)
    assert results[0]["crest_factor"] == pytest.approx(1.0)


def test_two_overlapping_windows():
    signal = np.ones(WINDOW_SIZE + STEP)

    results = extract_harmonized_multifeatures(signal)

    assert len(results) == 2
    assert [r["start_index"] for r in results] == [0, STEP]
    assert [r["end_index"] for r in results] == [
        WINDOW_SIZE - 1,
        WINDOW_SIZE + STEP - 1,
    ]


def test_rms_and_crest_factor_use_same_window():
    signal = np.ones(WINDOW_SIZE)
    signal[0] = 10.0

    result = extract_harmonized_multifeatures(signal)[0]

    expected_rms = np.sqrt(np.mean(signal ** 2))
    expected_cf = np.max(np.abs(signal)) / expected_rms

    assert result["rms"] == pytest.approx(expected_rms)
    assert result["crest_factor"] == pytest.approx(expected_cf)


@pytest.mark.parametrize("scale", [0.25, 0.5, 2.0, 10.0])
def test_positive_scaling_preserves_crest_factor(scale):
    signal = np.linspace(1.0, 3.0, WINDOW_SIZE)

    original = extract_harmonized_multifeatures(signal)[0]
    scaled = extract_harmonized_multifeatures(signal * scale)[0]

    assert scaled["rms"] == pytest.approx(
        original["rms"] * scale
    )
    assert scaled["crest_factor"] == pytest.approx(
        original["crest_factor"]
    )


def test_negative_scaling_preserves_crest_factor():
    signal = np.linspace(-2.0, 3.0, WINDOW_SIZE)

    original = extract_harmonized_multifeatures(signal)[0]
    inverted = extract_harmonized_multifeatures(-signal)[0]

    assert inverted["rms"] == pytest.approx(original["rms"])
    assert inverted["crest_factor"] == pytest.approx(
        original["crest_factor"]
    )


@pytest.mark.parametrize(
    "signal",
    [
        [],
        np.ones(1199),
        np.ones((1200, 1)),
        np.full(1200, np.nan),
        np.full(1200, np.inf),
        np.zeros(1200),
    ],
)
def test_invalid_or_undefined_signal(signal):
    with pytest.raises(ValueError):
        extract_harmonized_multifeatures(signal)
