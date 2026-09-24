from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.register_page.registerlocators import RegisterLocators
from pages.register_page.registerproperties import RegisterProperties


class RegisterPage(RegisterProperties, BasePage):
    def open(self):
        self.driver.get(self.SYSTEM_URL)

    def register(self, user: dict):
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
        self.wait.until(ec.text_to_be_present_in_element(RegisterLocators.SUCCESS_TITLE, "Welcome"))

    def wait_for_registration_outcome(self):
        """Waits for either the duplicate-username error or a successful "Welcome"
        heading, whichever the server actually renders, and returns which one it was.

        The live demo server occasionally does not render the duplicate-username
        error on the first submit - this makes that distinguishable from a real
        locator/timing bug instead of just timing out with no information.
        """
        def _outcome(driver):
            errors = driver.find_elements(*RegisterLocators.DUPLICATE_USERNAME_ERROR)
            if errors and errors[0].is_displayed():
                return ("error", errors[0].text)
            headings = driver.find_elements(*RegisterLocators.SUCCESS_TITLE)
            if headings and "Welcome" in headings[0].text:
                return ("success", headings[0].text)
            return False

        return self.wait.until(_outcome)
