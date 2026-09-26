import logging

from pages.bill_pay_page.billpaypage import BillPayPage
from testdata.billpaydata import PAYEE


def test_pay_bill_success(logged_in_driver):
    bill_pay_page = BillPayPage(logged_in_driver)
    bill_pay_page.open()

    bill_pay_page.pay_bill(PAYEE)

    bill_pay_page.wait_for_confirmation()
    actual_text = bill_pay_page.confirmation_title.text
    logging.info("Asserting 'Bill Payment Complete' is present in confirmation heading. Actual heading text: %r", actual_text)
    assert "Bill Payment Complete" in actual_text
