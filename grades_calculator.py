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
    sumofnumbers = 0
    for t in grades:
        sumofnumbers = sumofnumbers + t

    avg = sumofnumbers / len(grades)

    return round(avg, 2)

print("The average of recorded grades is", average([87,92,55,100,79]))


def drop_lowest(grades: List[float]) -> List[float]:
    """Drops the lowest number and returns the pruned collection

    Args:
        grades (List[float]): An array of number grades

    Returns:
        List[float]: The pruned list of grades
    """
    new_grades = grades.copy()
    new_grades.remove(min(new_grades))

    print(new_grades)

    return new_grades

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

    credit = 0.0

    for grade in grades :
        credit += weights[grade]

    final_grades = credit / len(grades)

    return round(final_grades, 2)
