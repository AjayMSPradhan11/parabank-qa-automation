from pages.base_page import BasePage
from pages.locators import BillPayPageLocators

SYSTEM_URL = "https://parabank.parasoft.com/parabank/billpay.htm"


class BillPayPage(BasePage):
    payee_name = BillPayPageLocators.PAYEE_NAME
    address = BillPayPageLocators.ADDRESS
    city = BillPayPageLocators.CITY
    state = BillPayPageLocators.STATE
    zip_code = BillPayPageLocators.ZIP_CODE
    phone = BillPayPageLocators.PHONE
    account_number = BillPayPageLocators.ACCOUNT_NUMBER
    verify_account_number = BillPayPageLocators.VERIFY_ACCOUNT_NUMBER
    amount = BillPayPageLocators.AMOUNT
    send_payment_button = BillPayPageLocators.SEND_PAYMENT_BUTTON
    confirmation_title = BillPayPageLocators.CONFIRMATION_TITLE

    def open(self):
        self.driver.get(SYSTEM_URL)

    def pay_bill(self, payee: dict):
        self.type(self.payee_name, payee["name"])
        self.type(self.address, payee["address"])
        self.type(self.city, payee["city"])
        self.type(self.state, payee["state"])
        self.type(self.zip_code, payee["zip_code"])
        self.type(self.phone, payee["phone"])
        self.type(self.account_number, payee["account_number"])
        self.type(self.verify_account_number, payee["account_number"])
        self.type(self.amount, payee["amount"])
        self.click(self.send_payment_button)
