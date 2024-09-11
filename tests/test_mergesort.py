from hw2_debugging import mergeSort

def test_ismergeworking():
    arr = [2,4,5,1,3]
    assert mergeSort(arr) == [1,2,3,4,5]  # This should pass



