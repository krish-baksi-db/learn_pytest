from typing import Optional, List, Union
import numpy as np

def sum(a: Union[int, float], b: Union[int, float]):
    """
    Adds two numbers
    Args:
        a: the first number.
        b: the second number.

    Returns:
        Union[int, float]: the sum of the input numbers.
    """

    return a + b


def difference(a: Union[int, float], b: Union[int, float]):
    """
    Finds the difference between two numbers.
    Args:
        a: the first number.
        b: the second number.

    Returns:
        Union[int, float]: the difference between the first and second numbers.
    """

    return a - b


def average(a: List[Union[float, int]]):
    """
    Finds average of a list of numbers
    Args:
        a: the list of numbers.

    Returns:
        Union[int, float]: the average of the numbers.    
    """
    if len(a):
        return np.mean(a)
    else:
        return None