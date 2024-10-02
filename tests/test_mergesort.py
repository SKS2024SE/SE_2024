import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from HW2.hw2_debugging import merge_sort

def test_ismergeworking():
    arr = [2,4,5,1,3]
    assert merge_sort(arr) == [1,2,3,4,5]  # This should pass


def test_already_ordered_arr():
    arr = [1,2,3,4,5,6,7,8,9,10]
    assert merge_sort(arr) == [1,2,3,4,5,6,7,8,9,10]  # This should pass

def test_reverse_ordered_arr():
    arr = [10,9,8,7,6,5,4,3,2,1,0]
    assert merge_sort(arr) == [0,1,2,3,4,5,6,7,8,9,10]  # This should pass
