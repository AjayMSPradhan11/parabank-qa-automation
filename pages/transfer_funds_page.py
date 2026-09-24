from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.locators import TransferFundsPageLocators

SYSTEM_URL = "https://parabank.parasoft.com/parabank/transfer.htm"


class TransferFundsPage(BasePage):
    amount_input = TransferFundsPageLocators.AMOUNT_INPUT
    from_account_select = TransferFundsPageLocators.FROM_ACCOUNT_SELECT
    to_account_select = TransferFundsPageLocators.TO_ACCOUNT_SELECT
    transfer_button = TransferFundsPageLocators.TRANSFER_BUTTON
    confirmation_title = TransferFundsPageLocators.CONFIRMATION_TITLE

    def open(self):
        self.driver.get(SYSTEM_URL)

    def wait_for_accounts_loaded(self):
        # fromAccountId/toAccountId are populated by an async AJAX call on page load
        self.wait.until(lambda d: len(Select(self.find(self.from_account_select)).options) > 0)

    def transfer(self, amount: str, from_account: str = None, to_account: str = None):
        self.wait_for_accounts_loaded()
        self.type(self.amount_input, amount)
        if from_account:
            Select(self.find(self.from_account_select)).select_by_visible_text(from_account)
        if to_account:
            Select(self.find(self.to_account_select)).select_by_visible_text(to_account)
        self.click(self.transfer_button)
