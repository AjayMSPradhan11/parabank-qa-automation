import logging

from pages.register_page.registerpage import RegisterPage
from testdata.logindata import EXISTING_USERNAME
from testdata.registerdata import new_user


def test_register_new_user_success(driver):
    register_page = RegisterPage(driver)
    register_page.open()

    user = new_user()
    register_page.register(user)

    register_page.wait_for_registration_success()
    actual_text = register_page.success_title.text
    logging.info("Asserting 'Welcome %s' is present in heading. Actual heading text: %r", user["username"], actual_text)
    assert f"Welcome {user['username']}" in actual_text


def test_register_with_existing_username_shows_error(driver):
    register_page = RegisterPage(driver)
    register_page.open()

    register_page.register(new_user(username=EXISTING_USERNAME))

    outcome, text = register_page.wait_for_registration_outcome()
    logging.info("Asserting outcome is 'error' with 'already exists' in message. Actual outcome: %r, message: %r", outcome, text)
    assert outcome == "error", f"expected duplicate-username error, server returned: {outcome} ({text!r})"
    assert "already exists" in text
