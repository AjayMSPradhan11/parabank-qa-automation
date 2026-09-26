import logging
import time

from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage, DEFAULT_TIMEOUT
from pages.register_page.registerlocators import RegisterLocators
from pages.register_page.registerproperties import RegisterProperties


class RegisterPage(RegisterProperties, BasePage):
    def open(self):
        logging.info("Opening register page")
        self.driver.get(self.SYSTEM_URL)

    def register(self, user: dict):
        logging.info("Registering new user: %s", user["username"])
        self.first_name.send_keys(user["first_name"])
        self.last_name.send_keys(user["last_name"])
        self.address.send_keys(user["address"])
        self.city.send_keys(user["city"])
        self.state.send_keys(user["state"])
        self.zip_code.send_keys(user["zip_code"])
        self.phone.send_keys(user["phone"])
        self.ssn.send_keys(user["ssn"])
        self.username.send_keys(user["username"])
        self.password.send_keys(user["password"])
        self.confirm_password.send_keys(user["password"])
        self.register_button.click()

    def wait_for_registration_success(self):
        # register.htm re-renders in place on success (no redirect/URL change) with
        # an h1 reading "Welcome <username>" - wait for that text, not just visibility,
        # since the pre-submit page already has a visible h1.title ("Signing up is easy!")
        logging.info("Waiting for registration success")
        self.wait.until(ec.text_to_be_present_in_element(RegisterLocators.SUCCESS_TITLE, "Welcome"))

    def wait_for_registration_outcome(self):
        # Polls for either the duplicate-username error or the success heading,
        # whichever the server actually renders - the live demo server occasionally
        # skips rendering the error on the first submit, so this distinguishes that
        # from a real locator/timing bug instead of just timing out with no information.
        logging.info("Waiting for registration outcome")
        end_time = time.time() + DEFAULT_TIMEOUT
        while time.time() < end_time:
            errors = self.driver.find_elements(*RegisterLocators.DUPLICATE_USERNAME_ERROR)
            if errors and errors[0].is_displayed():
                return "error", errors[0].text
            headings = self.driver.find_elements(*RegisterLocators.SUCCESS_TITLE)
            if headings and "Welcome" in headings[0].text:
                return "success", headings[0].text
            time.sleep(0.5)
        raise TimeoutError("Registration outcome not found within timeout")
