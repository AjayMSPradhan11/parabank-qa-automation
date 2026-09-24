from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log In']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error")
    ACCOUNTS_OVERVIEW_TITLE = (By.CSS_SELECTOR, "#rightPanel h1.title")
