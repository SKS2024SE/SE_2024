"""This file is to test the mergesort"""
import sys
import os

from hw2.hw2_debugging import merge_sort  # pylint: disable=E0401
# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


def test_ismergeworking():
    """Test that the merge_sort function correctly sorts an unsorted array."""
    arr = [2, 4, 5, 1, 3]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]  # This should pass

def test_already_ordered_arr():
    """Test that merge_sort returns the same array when the array is already ordered."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # This should pass

def test_reverse_ordered_arr():
    """Test that merge_sort correctly sorts a reverse-ordered array."""
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert merge_sort(arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # This should pass
