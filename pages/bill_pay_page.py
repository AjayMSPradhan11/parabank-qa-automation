from selenium.webdriver.common.by import By

from pages.base_page import BasePage

SYSTEM_URL = "https://parabank.parasoft.com/parabank/billpay.htm"


class BillPayPage(BasePage):
    payee_name = (By.NAME, "payee.name")
    address = (By.NAME, "payee.address.street")
    city = (By.NAME, "payee.address.city")
    state = (By.NAME, "payee.address.state")
    zip_code = (By.NAME, "payee.address.zipCode")
    phone = (By.NAME, "payee.phoneNumber")
    account_number = (By.NAME, "payee.accountNumber")
    verify_account_number = (By.NAME, "verifyAccount")
    amount = (By.NAME, "amount")
    send_payment_button = (By.XPATH, "//input[@value='Send Payment']")
    confirmation_title = (By.CSS_SELECTOR, "#billpayResult h1.title")

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
