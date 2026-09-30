import logging
import time

from pages.find_transfer_page.findtransferpage import FindTransferPage
from testdata.findtransferdata import INVALID_TRANSACTION, VALID_TRANSACTION

def test_find_transactions_with_valid_transaction(logged_in_driver):
    page = FindTransferPage(logged_in_driver)
    page.search_transaction(VALID_TRANSACTION["transaction_id"])
    time.sleep(2)

    assert VALID_TRANSACTION["expect_heading"] in page.get_results_heading()
    assert page.get_transaction_row_count() > 0

def test_find_transactions_with_invalid_transaction(logged_in_driver):
    page = FindTransferPage(logged_in_driver)
    page.search_transaction(INVALID_TRANSACTION["transaction_id"])
    time.sleep(2)

    assert INVALID_TRANSACTION["expect_message"] in page.get_transaction_id_error()