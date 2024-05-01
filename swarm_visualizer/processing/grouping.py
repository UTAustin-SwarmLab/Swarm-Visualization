"""Data Processing for grouping."""

from __future__ import annotations

import numpy as np


def group_values_by_bound(
    values: np.ndarray,
    step: float = 0.1,
    min_value: float = 0.0,
    max_value: float = 8.0,
    use_upper_bound: bool = True,
) -> np.ndarray:
    """
    Group values by replacing each with the nearest upper or lower bound defined by range steps.

    Args:
    values (list or np.array): List of values to be grouped.
    step (float): Step size for range intervals.
    min_value (float): Minimum value for the range intervals.
    max_value (float): Maximum value for the range intervals.
    use_upper_bound (bool): If True, group by upper bound, otherwise by lower bound.

    Returns:
    np.array: Array of values grouped by the specified bound of their range.
    """
    ranges = np.arange(min_value, max_value + step, step)
    group_list = []

    if use_upper_bound:
        for value in values:
            bound = next((x for x in ranges if x > value), None)
            if bound is not None:
                group_list.append(round(bound, 1))
            else:
                group_list.append(max_value)
    else:
        for value in values:
            bound = next((x for x in ranges[::-1] if x <= value), None)
            if bound is not None:
                group_list.append(round(bound, 1))
            else:
                group_list.append(max_value)

    return np.array(group_list)


def average_by_group(
    values: np.ndarray | list, group_keys: np.ndarray | list
) -> dict:
    if isinstance(values, list):
        values = np.array(values)

    if isinstance(group_keys, list):
        group_keys = np.array(group_keys)

    # Get unique groups and their indices
    unique_groups = np.unique(group_keys)
    average_results = {}

    for group in unique_groups:
        # Get the indices where group_keys equals the current group
        indices = np.where(group_keys == group)
        # Calculate the average for the current group
        average_results[group] = np.mean(values[indices])

    return average_results
