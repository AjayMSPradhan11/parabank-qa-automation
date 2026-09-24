from pages.bill_pay_page.billpaylocators import BillPayLocators


class BillPayProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/billpay.htm"

    @property
    def payee_name(self):
        return self.driver.find_element(*BillPayLocators.PAYEE_NAME)

    @property
    def address(self):
        return self.driver.find_element(*BillPayLocators.ADDRESS)

    @property
    def city(self):
        return self.driver.find_element(*BillPayLocators.CITY)

    @property
    def state(self):
        return self.driver.find_element(*BillPayLocators.STATE)

    @property
    def zip_code(self):
        return self.driver.find_element(*BillPayLocators.ZIP_CODE)

    @property
    def phone(self):
        return self.driver.find_element(*BillPayLocators.PHONE)

    @property
    def account_number(self):
        return self.driver.find_element(*BillPayLocators.ACCOUNT_NUMBER)

    @property
    def verify_account_number(self):
        return self.driver.find_element(*BillPayLocators.VERIFY_ACCOUNT_NUMBER)

    @property
    def amount(self):
        return self.driver.find_element(*BillPayLocators.AMOUNT)

    @property
    def send_payment_button(self):
        return self.driver.find_element(*BillPayLocators.SEND_PAYMENT_BUTTON)

    @property
    def confirmation_title(self):
        return self.driver.find_element(*BillPayLocators.CONFIRMATION_TITLE)
