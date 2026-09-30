import logging

from selenium.webdriver.support import expected_conditions

from pages.basepage import BasePage
from pages.request_loan_page.requestloanlocators import RequestLoanLocators
from pages.request_loan_page.requestloanproperties import RequestLoanProperties


class RequestLoanPage(RequestLoanProperties, BasePage):
    def open(self):
        logging.info("Opening request loan page")
        self.driver.get(self.SYSTEM_URL)

    def wait_for_accounts_loaded(self):
        logging.info("Waiting for from account dropdown to load")
        self.wait.until(expected_conditions.presence_of_element_located(RequestLoanLocators.ACCOUNT_OPTION))

    def request_loan(self, amount, down_payment):
        logging.info("Requesting loan amount %s with down payment %s", amount, down_payment)
        self.wait_for_accounts_loaded()
        self.loan_amount.clear()
        self.loan_amount.send_keys(amount)
        self.down_payment.clear()
        self.down_payment.send_keys(down_payment)
        self.apply_button.click()

    def get_result_heading(self):
        logging.info("Waiting for loan request result heading")
        self.wait.until(expected_conditions.visibility_of_element_located(RequestLoanLocators.RESULT_TITLE))
        heading = self.result_title
        return heading.text

    def get_loan_status(self):
        logging.info("Waiting for loan status")
        self.wait.until(expected_conditions.visibility_of_element_located(RequestLoanLocators.LOAN_STATUS))
        status = self.loan_status
        return status.text