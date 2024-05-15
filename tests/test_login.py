import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_invalid_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.open_home_page()
    home_page.click_sign_in()
    login_page.enter_email("test@example.com")
    login_page.enter_password("password")
    login_page.click_login_button()
    assert login_page._error_message

