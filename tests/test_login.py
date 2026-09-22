from pages.login_page import LoginPage
from tests.test_data import EXISTING_USERNAME, EXISTING_PASSWORD


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(EXISTING_USERNAME, EXISTING_PASSWORD)

    assert "Accounts Overview" in login_page.text_of(login_page.accounts_overview_title)


def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(EXISTING_USERNAME, "wrong_password_123")

    error_text = login_page.text_of(login_page.error_message)
    assert "could not be verified" in error_text
