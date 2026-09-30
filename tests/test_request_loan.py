import logging

from pages.request_loan_page.requestloanpage import RequestLoanPage
from testdata.requestloandata import APPROVED_LOAN, DENIED_LOAN


def test_request_loan_approved(logged_in_driver):
    page = RequestLoanPage(logged_in_driver)
    page.open()
    page.request_loan(APPROVED_LOAN["amount"], APPROVED_LOAN["down_payment"])

    actual_heading = page.get_result_heading()
    logging.info("Asserting %r is present in result heading. Actual heading: %r",
                 APPROVED_LOAN["expect_heading"], actual_heading)
    assert APPROVED_LOAN["expect_heading"] in actual_heading

    actual_status = page.get_loan_status()
    logging.info("Asserting loan status is %r. Actual status: %r", APPROVED_LOAN["expect_status"], actual_status)
    assert APPROVED_LOAN["expect_status"] in actual_status


def test_request_loan_denied(logged_in_driver):
    page = RequestLoanPage(logged_in_driver)
    page.open()
    page.request_loan(DENIED_LOAN["amount"], DENIED_LOAN["down_payment"])

    actual_heading = page.get_result_heading()
    logging.info("Asserting %r is present in result heading. Actual heading: %r",
                 DENIED_LOAN["expect_heading"], actual_heading)
    assert DENIED_LOAN["expect_heading"] in actual_heading

    actual_status = page.get_loan_status()
    logging.info("Asserting loan status is %r. Actual status: %r", DENIED_LOAN["expect_status"], actual_status)
    assert DENIED_LOAN["expect_status"] in actual_status