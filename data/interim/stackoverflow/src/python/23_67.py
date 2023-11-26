# 60.lastlinefromlargefile.py
# juanfc 2021-03-17

import os


def get_last_lines(fileName, offset=500):
    """ An efficient way to get the last lines of a file.

    IMPORTANT:
    1. Choose offset to be greater than
    max_line_length * number of lines that you want to recover.
    2. This will throw an os.OSError if the file is shorter than
    the offset.
    """
    with open(fileName, "rb") as f:
        f.seek(-offset, os.SEEK_END)
        return f.read().decode('utf-8').rstrip().split('\n')[-1]



print(get_last_lines('60.lastlinefromlargefile.py'))
