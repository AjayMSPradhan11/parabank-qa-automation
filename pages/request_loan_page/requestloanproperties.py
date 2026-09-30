from pages.request_loan_page.requestloanlocators import RequestLoanLocators


class RequestLoanProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/requestloan.htm"

    @property
    def loan_amount(self):
        return self.driver.find_element(*RequestLoanLocators.LOAN_AMOUNT)

    @property
    def down_payment(self):
        return self.driver.find_element(*RequestLoanLocators.DOWN_PAYMENT)

    @property
    def apply_button(self):
        return self.driver.find_element(*RequestLoanLocators.APPLY_BUTTON)

    @property
    def result_title(self):
        return self.driver.find_element(*RequestLoanLocators.RESULT_TITLE)

    @property
    def loan_status(self):
        return self.driver.find_element(*RequestLoanLocators.LOAN_STATUS)