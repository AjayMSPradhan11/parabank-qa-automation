import json
import logging
from pathlib import Path

from pages.bill_pay_page import BillPayPage

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent / "data"

with open(DATA_DIR / "bill_pay_payee.json") as f:
    PAYEE = json.load(f)


def test_pay_bill_success(logged_in_driver):
    bill_pay_page = BillPayPage(logged_in_driver)
    bill_pay_page.open()

    bill_pay_page.pay_bill(PAYEE)

    actual_text = bill_pay_page.text_of(bill_pay_page.confirmation_title)
    logger.info("Asserting 'Bill Payment Complete' is present in confirmation heading. Actual heading text: %r", actual_text)
    assert "Bill Payment Complete" in actual_text