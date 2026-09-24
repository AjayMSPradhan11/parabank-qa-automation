from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.bill_pay_page.billpaylocators import BillPayLocators
from pages.bill_pay_page.billpayproperties import BillPayProperties


class BillPayPage(BillPayProperties, BasePage):
    def open(self):
        self.driver.get(self.SYSTEM_URL)

    def pay_bill(self, payee: dict):
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
        self.wait.until(ec.visibility_of_element_located(BillPayLocators.CONFIRMATION_TITLE))
