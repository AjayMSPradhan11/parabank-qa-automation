from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.login_page.loginlocators import LoginLocators
from pages.login_page.loginproperties import LoginProperties


class LoginPage(LoginProperties, BasePage):
    def open(self):
        self.driver.get(self.SYSTEM_URL)

    def login(self, username, password):
        self.wait.until(ec.visibility_of_element_located(LoginLocators.USERNAME_INPUT))
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def wait_for_accounts_overview(self):
        self.wait.until(ec.visibility_of_element_located(LoginLocators.ACCOUNTS_OVERVIEW_TITLE))

    def wait_for_error_message(self):
        self.wait.until(ec.visibility_of_element_located(LoginLocators.ERROR_MESSAGE))
