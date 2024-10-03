"""Module providing a function printing python version.
Module is used to combine the results from the array."""

from hw2.rand import random_array # pylint: disable=E0401


def recombine(left_arr, right_arr):
    """Module providing a function printing python version.
Module is used to combine the results from the array."""
    left_index = 0
    right_index = 0

    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    return merge_arr


def merge_sort(arr_2):
    """This functions uses merge sort algorithm to sort the array."""
    if len(arr_2) == 1:
        return arr_2

    half = len(arr_2) // 2

    return recombine(merge_sort(arr_2[:half]), merge_sort(arr_2[half:]))


arr = random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
