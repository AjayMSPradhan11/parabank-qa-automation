from selenium.webdriver.common.by import By


class TransferFundsLocators:
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT_SELECT = (By.ID, "fromAccountId")
    TO_ACCOUNT_SELECT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, "#showResult h1.title")
