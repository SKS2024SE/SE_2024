"""Module providing a function printing python version."""

import subprocess

def random_array(arr):
    """Function to replace elements in the array with random numbers between 1 and 20."""
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False
        )
        arr[i] = int(shuffled_num.stdout)
    return arr

