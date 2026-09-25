import logging

from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.bill_pay_page.billpaylocators import BillPayLocators
from pages.bill_pay_page.billpayproperties import BillPayProperties

logger = logging.getLogger(__name__)


class BillPayPage(BillPayProperties, BasePage):
    def open(self):
        logger.info("Opening bill pay page")
        self.driver.get(self.SYSTEM_URL)

    def pay_bill(self, payee: dict):
        logger.info("Paying bill for payee: %s", payee["name"])
        self.payee_name.send_keys(payee["name"])
        self.address.send_keys(payee["address"])
        self.city.send_keys(payee["city"])
        self.state.send_keys(payee["state"])
        self.zip_code.send_keys(payee["zip_code"])
        self.phone.send_keys(payee["phone"])
        self.account_number.send_keys(payee["account_number"])
        self.verify_account_number.send_keys(payee["account_number"])
        self.amount.send_keys(payee["amount"])
        self.send_payment_button.click()

    def wait_for_confirmation(self):
        logger.info("Waiting for bill pay confirmation")
        self.wait.until(ec.visibility_of_element_located(BillPayLocators.CONFIRMATION_TITLE))
