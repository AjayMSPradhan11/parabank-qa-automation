from pages.login_page.loginlocators import LoginLocators


class LoginProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/index.htm"

    @property
    def username_input(self):
        return self.driver.find_element(*LoginLocators.USERNAME_INPUT)

    @property
    def password_input(self):
        return self.driver.find_element(*LoginLocators.PASSWORD_INPUT)

    @property
    def login_button(self):
        return self.driver.find_element(*LoginLocators.LOGIN_BUTTON)

    @property
    def error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE)

    @property
    def accounts_overview_title(self):
        return self.driver.find_element(*LoginLocators.ACCOUNTS_OVERVIEW_TITLE)
