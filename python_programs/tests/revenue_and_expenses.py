import pytest
from common_setup import run_test

def test_revenue_and_expenses():
    run_test("revenue_and_expenses", "Correct Revenue, Expenses, and Discretionary Calculations are Correct", "Error: Please make sure that your revenue, expenses and discretionary calculations are correct and outputted correctly")

if __name__ == '__main__':
    pytest.main()
