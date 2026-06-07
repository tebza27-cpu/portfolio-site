import subprocess
import requests
import json
import socket
import os
import platform
import sys
sys.path.append('..')
from central_setup.central_setup import (
    execute_logic,
    check_internet_connection,
    run_program,
    run_single_test,  # this function is called by the test files that import it from this file: common_setup.py
)

program_name = 'tracking_finances.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

def logic_gross_pay_calculation():
    """Test if the program correctly calculates gross pay."""
    # Test input parameters:
    # '1' - Option to calculate gross pay
    # '27.45' - Hourly wage in dollars
    # '160' - Total hours worked
    # '4' - Exit option after calculation
    return run_program(['1', '27.45', '160', '4'], program_name)

def logic_menu_and_input_validation():
    """Test if the program validates input correctly."""
    return run_program(['1', '4'], program_name)

def logic_revenue_and_expenses():
    """Test if the program correctly calculates revenue and expenses."""
    return run_program(['2', 'pay', '3460.90', 'y', 'rent', '-2200', '3', '4'], program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "gross_pay_calculation":
            test_outputs["gross_pay_calculation"] = logic_gross_pay_calculation()
        elif test_name == "menu_and_input_validation":
            test_outputs["menu_and_input_validation"] = logic_menu_and_input_validation()
        elif test_name == "revenue_and_expenses":
            test_outputs["revenue_and_expenses"] = logic_revenue_and_expenses()
    else:
        test_outputs = {
            "gross_pay_calculation": logic_gross_pay_calculation(),
            "menu_and_input_validation": logic_menu_and_input_validation(),
            "revenue_and_expenses": logic_revenue_and_expenses()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('tracking_finances.py', 'r') as f:
                student_code = f.read()
            with open('tests/test_tracking_finances.py', 'r') as f:
                pytest_code = f.read()
            with open('.github/classroom/autograding.json', 'r') as f:
                autograding_config = json.load(f)

            # Pass the logic to the central_setup module
            test_outputs, test_points_awarded, test_feedback, test_response_data = execute_logic(
                test_name, test_outputs, student_code, pytest_code, autograding_config
            )

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print("Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")

    return test_outputs, test_points_awarded, test_feedback, test_response_data