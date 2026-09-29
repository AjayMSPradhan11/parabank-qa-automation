import logging

from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.find_transfer_page.findtransferlocators import FindTransferLocators
from pages.find_transfer_page.findtransferproperties import FindTransferProperties


class FindTransferPage(FindTransferProperties, BasePage):
    def open(self):
        logging.info("Opening find transfer page")
        self.driver.get(self.SYSTEM_URL)

    def wait_for_accounts_loaded(self):
        # accountId is populated by an async AJAX call on page load
        logging.info("Waiting for account dropdown to load")
        self.wait.until(ec.presence_of_element_located(FindTransferLocators.ACCOUNT_OPTION))

    def find_by_transaction_id(self, transaction_id: str):
        # findtrans.htm builds this search as bank/transactions/{id}, so the account is not involved
        logging.info("Finding transactions by id: %s", transaction_id)
        self.transaction_id_input.send_keys(transaction_id)
        self.find_by_id_button.click()

    def find_by_date(self, account: str, transaction_date: str):
        logging.info("Finding transactions on date: %s", transaction_date)
        self.wait_for_accounts_loaded()
        self.account_select.select_by_value(account)
        self.transaction_date_input.send_keys(transaction_date)
        self.find_by_date_button.click()

    def find_by_date_range(self, account: str, from_date: str, to_date: str):
        logging.info("Finding transactions between %s and %s", from_date, to_date)
        self.wait_for_accounts_loaded()
        self.account_select.select_by_value(account)
        self.from_date_input.send_keys(from_date)
        self.to_date_input.send_keys(to_date)
        self.find_by_date_range_button.click()

    def find_by_amount(self, account: str, amount: str):
        logging.info("Finding transactions by amount: %s", amount)
        self.wait_for_accounts_loaded()
        self.account_select.select_by_value(account)
        self.amount_input.send_keys(amount)
        self.find_by_amount_button.click()

    def search_transaction(self, transaction_id: str):
        self.open()
        self.find_by_transaction_id(transaction_id)

    def wait_for_results(self):
        logging.info("Waiting for transactions results")
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.RESULTS_TITLE))

    def wait_for_transaction_id_error(self):
        logging.info("Waiting for transaction id error")
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.TRANSACTION_ID_ERROR))

    def wait_for_date_error(self):
        logging.info("Waiting for transaction date error")
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.TRANSACTION_DATE_ERROR))

    def wait_for_date_range_error(self):
        logging.info("Waiting for date range error")
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.DATE_RANGE_ERROR))

    def wait_for_amount_error(self):
        logging.info("Waiting for amount error")
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.AMOUNT_ERROR))

    def get_results_heading(self):
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.RESULTS_TITLE))
        text = self.results_title.text
        logging.info("Results heading text: %r", text)
        return text

    def get_transaction_row_count(self):
        count = len(self.transaction_rows)
        logging.info("Transaction row count: %d", count)
        return count

    def get_transaction_id_error(self):
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.TRANSACTION_ID_ERROR))
        text = self.transaction_id_error.text
        logging.info("Transaction ID error text: %r", text)
        return text

    def get_date_error(self):
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.TRANSACTION_DATE_ERROR))
        return self.transaction_date_error.text

    def get_date_range_error(self):
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.DATE_RANGE_ERROR))
        return self.date_range_error.text

    def get_amount_error(self):
        self.wait.until(ec.visibility_of_element_located(FindTransferLocators.AMOUNT_ERROR))
        return self.amount_error.text

