import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page.loginpage import LoginPage
from testdata.logindata import EXISTING_USERNAME, EXISTING_PASSWORD

logging.basicConfig(level=logging.INFO)


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Returns a driver already logged in as the seeded demo user (john/demo)."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(EXISTING_USERNAME, EXISTING_PASSWORD)
    login_page.wait_for_accounts_overview()
    return driver
