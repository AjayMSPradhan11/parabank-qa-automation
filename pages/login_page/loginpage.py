import logging

from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.login_page.loginlocators import LoginLocators
from pages.login_page.loginproperties import LoginProperties

logger = logging.getLogger(__name__)


class LoginPage(LoginProperties, BasePage):
    def open(self):
        logger.info("Opening login page")
        self.driver.get(self.SYSTEM_URL)

    def login(self, username, password):
        logger.info("Logging in user: %s", username)
        self.wait.until(ec.visibility_of_element_located(LoginLocators.USERNAME_INPUT))
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def wait_for_accounts_overview(self):
        logger.info("Waiting for accounts overview")
        self.wait.until(ec.visibility_of_element_located(LoginLocators.ACCOUNTS_OVERVIEW_TITLE))

    def wait_for_error_message(self):
        logger.info("Waiting for login error message")
        self.wait.until(ec.visibility_of_element_located(LoginLocators.ERROR_MESSAGE))
