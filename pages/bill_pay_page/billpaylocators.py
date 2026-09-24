from selenium.webdriver.common.by import By


class BillPayLocators:
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
