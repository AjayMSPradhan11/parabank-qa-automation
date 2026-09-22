from pages.transfer_funds_page import TransferFundsPage


def test_transfer_funds_success(logged_in_driver):
    transfer_page = TransferFundsPage(logged_in_driver)
    transfer_page.open()

    transfer_page.transfer(amount="10")

    assert "Transfer Complete" in transfer_page.text_of(transfer_page.confirmation_title)
