from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log In']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.error")
    ACCOUNTS_OVERVIEW_TITLE = (By.CSS_SELECTOR, "#rightPanel h1.title")


class RegisterPageLocators:
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")
    DUPLICATE_USERNAME_ERROR = (By.ID, "customer.username.errors")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#rightPanel h1.title")


class TransferFundsPageLocators:
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT_SELECT = (By.ID, "fromAccountId")
    TO_ACCOUNT_SELECT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, "#showResult h1.title")


class BillPayPageLocators:
    PAYEE_NAME = (By.NAME, "payee.name")
    ADDRESS = (By.NAME, "payee.address.street")
    CITY = (By.NAME, "payee.address.city")
    STATE = (By.NAME, "payee.address.state")
    ZIP_CODE = (By.NAME, "payee.address.zipCode")
    PHONE = (By.NAME, "payee.phoneNumber")
    ACCOUNT_NUMBER = (By.NAME, "payee.accountNumber")
    VERIFY_ACCOUNT_NUMBER = (By.NAME, "verifyAccount")
    AMOUNT = (By.NAME, "amount")
    SEND_PAYMENT_BUTTON = (By.XPATH, "//input[@value='Send Payment']")
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, "#billpayResult h1.title")
