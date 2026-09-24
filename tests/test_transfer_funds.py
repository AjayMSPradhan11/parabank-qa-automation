import logging
from pages.transfer_funds_page import TransferFundsPage

logger = logging.getLogger(__name__)

def test_transfer_funds_success(logged_in_driver):
    transfer_page = TransferFundsPage(logged_in_driver)
    transfer_page.open()

    transfer_page.transfer(amount="10")

    actual_text = transfer_page.text_of(transfer_page.confirmation_title)
    logger.info("Asserting 'Transfer Complete' is confirmation heading: %r", actual_text)
    assert "Transfer Complete" in actual_text

