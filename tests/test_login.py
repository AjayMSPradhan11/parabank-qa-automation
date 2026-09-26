import logging

from pages.login_page.loginpage import LoginPage
from testdata.logindata import LOGIN_CASES

LOGIN_CASES_BY_ID = {case["id"]: case for case in LOGIN_CASES}


def test_login_with_valid_credentials(driver):
    case = LOGIN_CASES_BY_ID["valid_login"]

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(case["username"], case["password"])
    login_page.wait_for_accounts_overview()

    actual_text = login_page.accounts_overview_title.text
    logging.info("Asserting 'Accounts Overview' is present in heading. Actual heading text: %r", actual_text)
    assert "Accounts Overview" in actual_text


def test_login_with_invalid_credentials(driver):
    case = LOGIN_CASES_BY_ID["wrong_password"]

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(case["username"], case["password"])
    login_page.wait_for_error_message()

    error_text = login_page.error_message.text
    logging.info("Asserting error message contains %r. Actual error text: %r", case["expect_message"], error_text)
    assert case["expect_message"] in error_text
