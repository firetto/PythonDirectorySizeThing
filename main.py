"""
PythonDirectorySizeThing

Includes functions to do the task.

Anatoly Zavyalov
"""

import os


def get_largest_files_new(directory: str, num: int) -> list:
    """
    Return a sorted list containing up to num of the largest files from the directory.

    Preconditions:
     - num > 0
    """

    # ACCUMULATOR: Priority queue so far
    list_so_far = []

    for root in os.walk(directory):
        path = root[0]
        for file in root[2]:
            try:
                list_so_far.append((os.path.getsize(os.path.join(path, file)), os.path.join(path, file)))
            except FileNotFoundError:
                print("Couldn't find file at ", os.path.join(path, file))

    return sorted(list_so_far)[-num:]
