from selenium.webdriver.support import expected_conditions

from pages.basepage import BasePage
from pages.find_transfer_page.findtransferlocators import FindTransferLocators
from pages.find_transfer_page.findtransferproperties import FindTransferProperties


class FindTransferPage(FindTransferProperties, BasePage):
    def open(self):
        self.driver.get(self.SYSTEM_URL)

    def find_by_transaction_id(self, transaction_id):
        self.transaction_id_input.send_keys(transaction_id)
        self.find_by_id_button.click()

    def search_transaction(self, transaction_id):
        self.open()
        self.find_by_transaction_id(transaction_id)

    def get_results_heading(self):
        self.wait.until(expected_conditions.visibility_of_element_located(FindTransferLocators.RESULTS_TITLE))
        heading = self.results_title
        return heading.text

    def get_transaction_row_count(self):
        rows = self.transaction_rows
        return len(rows)

    def get_transaction_id_error(self):
        self.wait.until(expected_conditions.visibility_of_element_located(FindTransferLocators.TRANSACTION_ID_ERROR))
        error = self.transaction_id_error
        return error.text