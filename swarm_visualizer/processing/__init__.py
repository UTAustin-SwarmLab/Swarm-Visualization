"""Package containing for processing data."""

from __future__ import annotations

from .grouping import average_by_group, group_values_by_bound
from .sorting import sort_array_based_on_reference_array

__all__ = [
    "group_values_by_bound",
    "sort_array_based_on_reference_array",
    "average_by_group",
]
