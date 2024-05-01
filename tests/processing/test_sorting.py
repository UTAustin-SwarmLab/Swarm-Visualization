import numpy as np
import pytest

from swarm_visualizer.processing import (
    sort_array_based_on_reference_array,  # Replace 'your_module' with the actual name of your module
)


# Define a fixture for the sample data
@pytest.fixture
def sample_data():
    data = {
        "prices": np.array([20.95, 15.99, 22.50, 18.00]),
        "ratings": np.array([4.5, 3.8, 4.9, 4.0]),
        "stocks": np.array([34, 42, 25, 50]),
    }
    return data


def test_sort_ascending(sample_data):
    """Test sorting arrays in ascending order based on ratings."""
    sorted_arrays = sort_array_based_on_reference_array(
        [sample_data["prices"], sample_data["stocks"]],
        sample_data["ratings"],
        "ascending",
    )
    expected_ratings_sorted = np.array([3.8, 4.0, 4.5, 4.9])
    expected_prices_sorted = np.array([15.99, 18.00, 20.95, 22.50])
    expected_stocks_sorted = np.array([42, 50, 34, 25])

    np.testing.assert_array_equal(sorted_arrays[0], expected_ratings_sorted)
    np.testing.assert_array_equal(sorted_arrays[1], expected_prices_sorted)
    np.testing.assert_array_equal(sorted_arrays[2], expected_stocks_sorted)


def test_sort_descending(sample_data):
    """Test sorting arrays in descending order based on ratings."""
    sorted_arrays = sort_array_based_on_reference_array(
        [sample_data["prices"], sample_data["stocks"]],
        sample_data["ratings"],
        "descending",
    )
    expected_ratings_sorted = np.array([4.9, 4.5, 4.0, 3.8])
    expected_prices_sorted = np.array([22.50, 20.95, 18.00, 15.99])
    expected_stocks_sorted = np.array([25, 34, 50, 42])

    np.testing.assert_array_equal(sorted_arrays[0], expected_ratings_sorted)
    np.testing.assert_array_equal(sorted_arrays[1], expected_prices_sorted)
    np.testing.assert_array_equal(sorted_arrays[2], expected_stocks_sorted)


def test_length_mismatch(sample_data):
    """Test error raising when input arrays do not have the same length."""
    with pytest.raises(ValueError):
        sort_array_based_on_reference_array(
            [sample_data["prices"], np.array([1, 2])],
            sample_data["ratings"],
            "ascending",
        )
