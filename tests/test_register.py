from pages.register_page import RegisterPage
from tests.test_data import EXISTING_USERNAME, new_user


def test_register_new_user_success(driver):
    register_page = RegisterPage(driver)
    register_page.open()

    user = new_user()
    register_page.register(user)

    register_page.wait_for_registration_success()
    assert f"Welcome {user['username']}" in register_page.text_of(register_page.success_title)


def test_register_with_existing_username_shows_error(driver):
    register_page = RegisterPage(driver)
    register_page.open()

    register_page.register(new_user(username=EXISTING_USERNAME))

    outcome, text = register_page.wait_for_registration_outcome()
    assert outcome == "error", f"expected duplicate-username error, server returned: {outcome} ({text!r})"
    assert "already exists" in text
