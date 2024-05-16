"""Data Processing for sorting."""

from __future__ import annotations

import numpy as np


def sort_array_based_on_reference_array(
    list_of_arrays: list[np.ndarray],
    reference_array: np.ndarray,
    order: str = "ascending",
) -> list[np.ndarray]:
    """
    Sort multiple arrays based on the values of a single reference array, with an option to sort in ascending or descending order.

    Args:
    - list_of_arrays (list[np.ndarray]): List of arrays to be sorted including the reference array.
    - reference_array (np.ndarray): The reference array that dictates the sort order.
    - order (str): Sorting order, 'ascending' or 'descending'. Default is 'ascending'.

    Returns:
    - list[np.ndarray]: List of sorted arrays including the reference array.
    """
    # Include reference_array in the list for sorting
    list_of_arrays = [reference_array] + list_of_arrays

    if not all(len(arr) == len(reference_array) for arr in list_of_arrays):
        raise ValueError(
            "All arrays must have the same length as the reference array."
        )

    # Create tuples of indexes and reference array values
    indexed_pairs = list(enumerate(reference_array))

    # Sort indexed pairs based on reference values
    indexed_pairs_sorted = sorted(
        indexed_pairs, key=lambda x: x[1], reverse=(order == "descending")
    )

    # Reorder each array in the list according to the sorted indexes
    sorted_arrays = [
        np.array([array[idx] for idx, _ in indexed_pairs_sorted])
        for array in list_of_arrays
    ]

    return sorted_arrays
