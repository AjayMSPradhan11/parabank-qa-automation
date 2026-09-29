from selenium.webdriver.common.by import By


class FindTransferLocators:
    ACCOUNT_SELECT = (By.ID, "accountId")
    ACCOUNT_OPTION = (By.CSS_SELECTOR, "#accountId option")
    TRANSACTION_ID_INPUT = (By.ID, "transactionId")
    TRANSACTION_DATE_INPUT = (By.ID, "transactionDate")
    FROM_DATE_INPUT = (By.ID, "fromDate")
    TO_DATE_INPUT = (By.ID, "toDate")
    AMOUNT_INPUT = (By.ID, "amount")
    FIND_BY_ID_BUTTON = (By.ID, "findById")
    FIND_BY_DATE_BUTTON = (By.ID, "findByDate")
    FIND_BY_DATE_RANGE_BUTTON = (By.ID, "findByDateRange")
    FIND_BY_AMOUNT_BUTTON = (By.ID, "findByAmount")
    TRANSACTION_ID_ERROR = (By.ID, "transactionIdError")
    TRANSACTION_DATE_ERROR = (By.ID, "transactionDateError")
    DATE_RANGE_ERROR = (By.ID, "dateRangeError")
    AMOUNT_ERROR = (By.ID, "amountError")
    RESULTS_TITLE = (By.CSS_SELECTOR, "#resultContainer h1.title")
    TRANSACTIONS_TABLE = (By.ID, "transactionTable")
    TRANSACTION_ROW = (By.CSS_SELECTOR, "#transactionBody tr")