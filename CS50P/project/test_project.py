import pytest
from project import custom_function1, custom_function2  # Import your functions from project.py


# Test function for custom_function1
def test_custom_function1():
    # Test cases for custom_function1
    assert custom_function1(input_data) == expected_output  # Replace input_data and expected_output with actual test data


# Test function for custom_function2
def test_custom_function2():
    # Test cases for custom_function2
    assert custom_function2(input_data) == expected_output  # Replace input_data and expected_output with actual test data


# You should have test functions for each custom function you've implemented in project.py
