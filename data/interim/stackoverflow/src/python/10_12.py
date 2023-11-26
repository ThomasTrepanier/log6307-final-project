import numpy as np


def to_numeric1(array, sep=' ', dtype=np.float):
    """
    Converts an array of strings with delimiters in it 
    to an array of specified type
    """
    split = np.char.split(array, sep=sep)
    without_lists = np.array(split.tolist())
    corrected_dimension = np.squeeze(without_lists)
    return corrected_dimension.astype(dtype)
