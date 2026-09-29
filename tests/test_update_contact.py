import logging

from pages.update_contact_page.updatecontactpage import UpdateContactPage
from testdata.updatecontactdata import INVALID_CONTACT, VALID_CONTACT


def test_update_contact_with_valid_data(logged_in_driver):
    page = UpdateContactPage(logged_in_driver)
    page.open()
    page.update_contact(VALID_CONTACT["first_name"], VALID_CONTACT["last_name"], VALID_CONTACT["address"],
                        VALID_CONTACT["city"], VALID_CONTACT["state"], VALID_CONTACT["zip_code"],
                        VALID_CONTACT["phone"])

    actual_heading = page.get_result_heading()
    logging.info("Asserting %r is present in result heading. Actual heading: %r",
                 VALID_CONTACT["expect_heading"], actual_heading)
    assert VALID_CONTACT["expect_heading"] in actual_heading


def test_update_contact_with_empty_first_name(logged_in_driver):
    page = UpdateContactPage(logged_in_driver)
    page.open()
    page.update_contact(INVALID_CONTACT["first_name"], INVALID_CONTACT["last_name"], INVALID_CONTACT["address"],
                        INVALID_CONTACT["city"], INVALID_CONTACT["state"], INVALID_CONTACT["zip_code"],
                        INVALID_CONTACT["phone"])

    actual_error = page.get_first_name_error()
    logging.info("Asserting %r is present in error message. Actual error: %r",
                 INVALID_CONTACT["expect_message"], actual_error)
    assert INVALID_CONTACT["expect_message"] in actual_error