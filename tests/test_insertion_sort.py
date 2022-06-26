"""Tests for insertion sort."""
from algorithms.insertion_sort import insertion_sort


def test_insertion_sort():
    """Test insertion sort."""
    shuffled = [5, 2, 1, 6, 4, 3]
    in_order = [1, 2, 3, 4, 5, 6]

    insertion_sort(shuffled)

    assert in_order == shuffled
