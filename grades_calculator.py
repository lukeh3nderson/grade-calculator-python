"""
This is a library of functions designed to be useful in a
variety of different types of grade calculations.
"""

# import support for type hinting the functions
from typing import List, Dict

def average(grades: List[float]) -> float:
    """Calculates the average of an array of grades, rounded to 2 decimal places

    Args:
        grades (List[float]): An array of number grades

    Returns:
        float: The average of the grades
    """
    return 0

def drop_lowest(grades: List[float]) -> List[float]:
    """Drops the lowest number and returns the pruned collection

    Args:
        grades (List[float]): An array of number grades

    Returns:
        List[float]: The pruned list of grades
    """
    return []

def calculate_gpa(grades: List[str], weights: Dict[str, float]) -> float:
    """
    Takes a list of letter grades, and a dictionary that provides
    the relative weights of those letter grades in GPA format. It
    calculates a GPA based on the number of grades and their weights
    rounded to two decimal places.

    Args:
        grades (List[str]): A list of letter grades, e.g. A, B+, C, A-, etc.
        weights (Dict[str, float]): The dictionary equating letter grades to their weight

    Returns:
        float: The calculated GPA
    """
    return 0
