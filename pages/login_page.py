from selenium.webdriver.common.by import By

from pages.base_page import BasePage

SYSTEM_URL = "https://parabank.parasoft.com/parabank/index.htm"


class LoginPage(BasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "input[value='Log In']")
    error_message = (By.CSS_SELECTOR, "p.error")
    accounts_overview_title = (By.CSS_SELECTOR, "#rightPanel h1.title")

    def open(self):
        self.driver.get(SYSTEM_URL)

    def login(self, username: str, password: str):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)
