import logging

from pages.login_page.loginpage import LoginPage
from testdata.logindata import EXISTING_USERNAME, EXISTING_PASSWORD, LOGIN_CASES

logger = logging.getLogger(__name__)

LOGIN_CASES_BY_ID = {case["id"]: case for case in LOGIN_CASES}


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(EXISTING_USERNAME, EXISTING_PASSWORD)
    login_page.wait_for_accounts_overview()

    actual_text = login_page.accounts_overview_title.text
    logger.info("Asserting 'Accounts Overview' is present in heading. Actual heading text: %r", actual_text)
    assert "Accounts Overview" in actual_text


def test_login_with_invalid_credentials(driver):
    case = LOGIN_CASES_BY_ID["wrong_password"]

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(case["username"], case["password"])
    login_page.wait_for_error_message()

    error_text = login_page.error_message.text
    logger.info("Asserting error message contains %r. Actual error text: %r", case["expect_message"], error_text)
    assert case["expect_message"] in error_text
