from pages.login_page import LoginPage
from pages.home_page import HomePage
from factory.test_data import TestData


def test_fast_home_page(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    test_data = TestData()

    # Create test data before test
    test_data.create_test_group_and_item_data()

    login_page.perform_login_operation()
    home_page.check_basic_elements_on_page()
    home_page.perform_logout_operation()

    # Delete test data after test
    test_data.delete_test_group_data()