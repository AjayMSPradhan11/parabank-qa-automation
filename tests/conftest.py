import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from tests.test_data import EXISTING_USERNAME, EXISTING_PASSWORD

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
    login_page.find(login_page.accounts_overview_title)
    return driver
