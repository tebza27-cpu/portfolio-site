from common_setup import run_test

def test_menu_and_input_validation():
    run_test("menu_and_input_validation", "Functional Menu Navigation", "Error: Make sure that you can navigate through your program as seen in the sample output in Canvas")

if __name__ == '__main__':
    pytest.main()