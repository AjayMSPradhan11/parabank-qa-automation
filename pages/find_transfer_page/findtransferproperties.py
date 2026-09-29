from selenium.webdriver.support.ui import Select

from pages.find_transfer_page.findtransferlocators import FindTransferLocators


class FindTransferProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/findtrans.htm"

    @property
    def account_select(self):
        return Select(self.driver.find_element(*FindTransferLocators.ACCOUNT_SELECT))

    @property
    def transaction_id_input(self):
        return self.driver.find_element(*FindTransferLocators.TRANSACTION_ID_INPUT)

    @property
    def transaction_date_input(self):
        return self.driver.find_element(*FindTransferLocators.TRANSACTION_DATE_INPUT)

    @property
    def from_date_input(self):
        return self.driver.find_element(*FindTransferLocators.FROM_DATE_INPUT)

    @property
    def to_date_input(self):
        return self.driver.find_element(*FindTransferLocators.TO_DATE_INPUT)

    @property
    def amount_input(self):
        return self.driver.find_element(*FindTransferLocators.AMOUNT_INPUT)

    @property
    def find_by_id_button(self):
        return self.driver.find_element(*FindTransferLocators.FIND_BY_ID_BUTTON)

    @property
    def find_by_date_button(self):
        return self.driver.find_element(*FindTransferLocators.FIND_BY_DATE_BUTTON)

    @property
    def find_by_date_range_button(self):
        return self.driver.find_element(*FindTransferLocators.FIND_BY_DATE_RANGE_BUTTON)

    @property
    def find_by_amount_button(self):
        return self.driver.find_element(*FindTransferLocators.FIND_BY_AMOUNT_BUTTON)

    @property
    def transaction_id_error(self):
        return self.driver.find_element(*FindTransferLocators.TRANSACTION_ID_ERROR)

    @property
    def transaction_date_error(self):
        return self.driver.find_element(*FindTransferLocators.TRANSACTION_DATE_ERROR)

    @property
    def date_range_error(self):
        return self.driver.find_element(*FindTransferLocators.DATE_RANGE_ERROR)

    @property
    def amount_error(self):
        return self.driver.find_element(*FindTransferLocators.AMOUNT_ERROR)

    @property
    def results_title(self):
        return self.driver.find_element(*FindTransferLocators.RESULTS_TITLE)

    @property
    def transactions_table(self):
        return self.driver.find_element(*FindTransferLocators.TRANSACTIONS_TABLE)

    @property
    def transaction_rows(self):
        return self.driver.find_elements(*FindTransferLocators.TRANSACTION_ROW)


