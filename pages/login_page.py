from pages.base_page import BasePage
from pages.locators import LoginPageLocators

SYSTEM_URL = "https://parabank.parasoft.com/parabank/index.htm"


class LoginPage(BasePage):
    username_input = LoginPageLocators.USERNAME_INPUT
    password_input = LoginPageLocators.PASSWORD_INPUT
    login_button = LoginPageLocators.LOGIN_BUTTON
    error_message = LoginPageLocators.ERROR_MESSAGE
    accounts_overview_title = LoginPageLocators.ACCOUNTS_OVERVIEW_TITLE

    def open(self):
        self.driver.get(SYSTEM_URL)

    def login(self, username: str, password: str):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)
