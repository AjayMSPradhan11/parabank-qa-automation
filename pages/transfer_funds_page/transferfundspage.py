import logging

from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.transfer_funds_page.transferfundslocators import TransferFundsLocators
from pages.transfer_funds_page.transferfundsproperties import TransferFundsProperties


class TransferFundsPage(TransferFundsProperties, BasePage):
    def open(self):
        logging.info("Opening transfer funds page")
        self.driver.get(self.SYSTEM_URL)

    def wait_for_accounts_loaded(self):
        # fromAccountId/toAccountId are populated by an async AJAX call on page load
        logging.info("Waiting for account dropdowns to load")
        self.wait.until(ec.presence_of_element_located(TransferFundsLocators.FROM_ACCOUNT_OPTION))

    def transfer(self, amount: str, from_account: str = None, to_account: str = None):
        logging.info("Transferring amount: %s", amount)
        self.wait_for_accounts_loaded()
        self.amount_input.send_keys(amount)
        if from_account:
            self.from_account_select.select_by_visible_text(from_account)
        if to_account:
            self.to_account_select.select_by_visible_text(to_account)
        self.transfer_button.click()

    def wait_for_confirmation(self):
        logging.info("Waiting for transfer confirmation")
        self.wait.until(ec.visibility_of_element_located(TransferFundsLocators.CONFIRMATION_TITLE))
