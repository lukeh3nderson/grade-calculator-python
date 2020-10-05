"""
DO NOT ALTER THIS FILE!!!
This file contains a set of unit tests describing the functions
that will be a part of a library of grade calculation functions.
Your job is to write the code in grade-calculator.js to make ALL
of these tests pass.
"""
# pylint: disable=unused-variable

# import the functions to be tested
from grades_calculator import average, drop_lowest, calculate_gpa

def describe_a_library_of_grade_calculation_functions():
    """Our test suite"""

    def can_blow_smoke():
        assert True

    def can_calculate_an_average():
        # given this hypothetical list of grades
        grades = [87, 92, 55, 100, 79]
        assert average(grades) == 82.6
        # given this different set of grades
        grades = [99, 24, 75.2, 84, 87, 82]
        assert average(grades) == 75.2

    def can_drop_the_lowest_grade_from_a_set():
        # given this hypothetical list of grades
        grades = [87, 92, 55, 100, 79]
        assert drop_lowest(grades) == [87, 92, 100, 79]
        assert len(drop_lowest(grades)) == 4
        # given this different set of grades
        grades = [99, 24, 75.2, 84, 87, 82]
        assert drop_lowest(grades) == [99, 75.2, 84, 87, 82]
        assert len(drop_lowest(grades)) == 5

    def can_calculate_a_gpa():
        weights = {
            'A': 4,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1,
            'D-': 0.7,
            'F': 0,
        }
        # for this set of grades
        grades = ['A', 'B-', 'C+', 'B', 'B', 'F']
        assert calculate_gpa(grades, weights) == 2.4
        # and for this other set of grades
        grades = ['D+', 'C', 'C', 'B+', 'A-', 'A-', 'A']
        assert calculate_gpa(grades, weights) == 2.88
