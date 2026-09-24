import logging
import json
from pathlib import Path

from pages.login_page import LoginPage
from tests.test_data import EXISTING_USERNAME, EXISTING_PASSWORD

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent / "data"

with open(DATA_DIR / "login_cases.json") as f:
    LOGIN_CASES = {case["id"]: case for case in json.load(f)}

def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(EXISTING_USERNAME, EXISTING_PASSWORD)

    actual_text = login_page.text_of(login_page.accounts_overview_title)
    logger.info("Asserting 'Accounts Overview' is present in heading. Actual heading text: %r", actual_text)
    assert "Accounts Overview" in actual_text


def test_login_with_invalid_credentials(driver):
    case = LOGIN_CASES["wrong_password"]

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(case["username"], case["password"])

    error_text = login_page.text_of(login_page.error_message)
    logger.info("Asserting error message contains %r. Actual error text: %r", case["expect_message"], error_text)
    assert case["expect_message"] in error_text
