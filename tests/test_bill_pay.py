import logging
import time

from pages.bill_pay_page.billpaypage import BillPayPage
from testdata.billpaydata import PAYEE, BILL_PAY_CASES


def test_pay_bill_success(logged_in_driver):
    bill_pay_page = BillPayPage(logged_in_driver)
    bill_pay_page.open()

    bill_pay_page.pay_bill(PAYEE)
    time.sleep(2)

    bill_pay_page.wait_for_confirmation()
    actual_text = bill_pay_page.confirmation_title.text
    logging.info("Asserting 'Bill Payment Complete' is present in confirmation heading. Actual heading text: %r", actual_text)
    assert "Bill Payment Complete" in actual_text

def test_pay_bill_invalid(logged_in_driver):
    bill_pay_page = BillPayPage(logged_in_driver)
    bill_pay_page.open()

    bill_pay_page.pay_bill(BILL_PAY_CASES[0])
    time.sleep(2)

    bill_pay_page.wait_for_error()
    actual_text = bill_pay_page.error_message.text
    logging.info("Asserting expected message is present in error text. Actual text: %r", actual_text)
    assert BILL_PAY_CASES[0]["expect_message"] in actual_text