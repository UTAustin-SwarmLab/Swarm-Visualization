import numpy as np
import pytest

from swarm_visualizer.processing import group_values_by_bound


def test_group_values_by_upper_bound():
    values = np.array([0.05, 0.15, 0.25, 0.8])
    expected = np.array([0.1, 0.2, 0.3, 0.9])
    assert np.array_equal(
        group_values_by_bound(values, step=0.1, min_value=0, max_value=1),
        expected,
    )


def test_group_values_by_lower_bound():
    values = np.array([0.05, 0.15, 0.25, 0.8])
    expected = np.array([0.0, 0.1, 0.2, 0.8])
    assert np.array_equal(
        group_values_by_bound(
            values, step=0.1, min_value=0, max_value=1, use_upper_bound=False
        ),
        expected,
    )


def test_empty_input():
    values = np.array([])
    expected = np.array([])
    assert np.array_equal(
        group_values_by_bound(values, step=0.1, min_value=0, max_value=1),
        expected,
    )


def test_non_numeric_input():
    with pytest.raises(TypeError):
        group_values_by_bound(
            ["a", "b", "c"], step=0.1, min_value=0, max_value=1
        )
