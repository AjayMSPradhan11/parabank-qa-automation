import logging

from pages.transfer_funds_page.transferfundspage import TransferFundsPage

logger = logging.getLogger(__name__)


def test_transfer_funds_success(logged_in_driver):
    transfer_page = TransferFundsPage(logged_in_driver)
    transfer_page.open()

    transfer_page.transfer(amount="10")

    transfer_page.wait_for_confirmation()
    actual_text = transfer_page.confirmation_title.text
    logger.info("Asserting 'Transfer Complete' is confirmation heading. Actual heading text: %r", actual_text)
    assert "Transfer Complete" in actual_text
