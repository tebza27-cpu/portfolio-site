from common_setup import run_test

def test_gross_pay_calculation():
    run_test("gross_pay_calculation", "Gross Pay Calculation is Correct", "Error: Please ensure that your Gross Pay Calculations are correct and out displaying properly as in the example output on Canvas.")

if __name__ == '__main__':
    pytest.main()
