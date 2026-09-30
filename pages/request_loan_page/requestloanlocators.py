from selenium.webdriver.common.by import By


class RequestLoanLocators:
    LOAN_AMOUNT = (By.ID, "amount")
    DOWN_PAYMENT = (By.ID, "downPayment")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    ACCOUNT_OPTION = (By.CSS_SELECTOR, "#fromAccountId option")
    APPLY_BUTTON = (By.CSS_SELECTOR, "input[value='Apply Now']")
    RESULT_TITLE = (By.XPATH, "//h1[contains(text(), 'Loan Request Processed')]")
    LOAN_STATUS = (By.ID, "loanStatus")