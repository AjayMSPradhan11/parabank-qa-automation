import logging
import time

from pages.bill_pay_page.billpaypage import BillPayPage
from pages.find_transfer_page.findtransferpage import FindTransferPage
from pages.request_loan_page.requestloanpage import RequestLoanPage
from pages.transfer_funds_page.transferfundspage import TransferFundsPage
from testdata.billpaydata import PAYEE
from testdata.findtransferdata import VALID_TRANSACTION
from testdata.requestloandata import APPROVED_LOAN
from testdata.transferfundsdata import TRANSFER_AMOUNT


def test_transfer_then_pay_bill_then_request_loan_then_find_transfer(logged_in_driver):
    transfer_page = TransferFundsPage(logged_in_driver)
    transfer_page.open()
    time.sleep(2)

    accounts = transfer_page.get_available_accounts()
    transfer_page.transfer(amount=TRANSFER_AMOUNT, from_account=accounts[0], to_account=accounts[1])
    transfer_page.wait_for_confirmation()
    time.sleep(3)

    bill_pay_page = BillPayPage(logged_in_driver)
    bill_pay_page.open()
    time.sleep(2)

    bill_pay_page.pay_bill(PAYEE)
    bill_pay_page.wait_for_confirmation()
    time.sleep(3)

    actual_text = bill_pay_page.confirmation_title.text
    logging.info("Asserting 'Bill Payment Complete' is present. Actual heading text: %r", actual_text)
    assert "Bill Payment Complete" in actual_text

    loan_page = RequestLoanPage(logged_in_driver)
    loan_page.open()
    time.sleep(2)

    loan_page.request_loan(APPROVED_LOAN["amount"], APPROVED_LOAN["down_payment"])
    actual_heading = loan_page.get_result_heading()
    time.sleep(3)

    logging.info("Asserting %r is present in result heading. Actual heading: %r",
                 APPROVED_LOAN["expect_heading"], actual_heading)
    assert APPROVED_LOAN["expect_heading"] in actual_heading

    find_transfer_page = FindTransferPage(logged_in_driver)
    find_transfer_page.search_transaction(VALID_TRANSACTION["transaction_id"])
    time.sleep(2)

    actual_results_heading = find_transfer_page.get_results_heading()
    logging.info("Asserting %r is present in results heading. Actual heading: %r",
                 VALID_TRANSACTION["expect_heading"], actual_results_heading)
    assert VALID_TRANSACTION["expect_heading"] in actual_results_heading
    assert find_transfer_page.get_transaction_row_count() > 0