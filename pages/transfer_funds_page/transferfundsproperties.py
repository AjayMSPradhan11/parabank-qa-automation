from selenium.webdriver.support.ui import Select

from pages.transfer_funds_page.transferfundslocators import TransferFundsLocators


class TransferFundsProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/transfer.htm"

    @property
    def amount_input(self):
        return self.driver.find_element(*TransferFundsLocators.AMOUNT_INPUT)

    @property
    def from_account_select(self):
        return Select(self.driver.find_element(*TransferFundsLocators.FROM_ACCOUNT_SELECT))

    @property
    def to_account_select(self):
        return Select(self.driver.find_element(*TransferFundsLocators.TO_ACCOUNT_SELECT))

    @property
    def transfer_button(self):
        return self.driver.find_element(*TransferFundsLocators.TRANSFER_BUTTON)

    @property
    def confirmation_title(self):
        return self.driver.find_element(*TransferFundsLocators.CONFIRMATION_TITLE)
