from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.locators import RegisterPageLocators

SYSTEM_URL = "https://parabank.parasoft.com/parabank/register.htm"


class RegisterPage(BasePage):
    first_name = RegisterPageLocators.FIRST_NAME
    last_name = RegisterPageLocators.LAST_NAME
    address = RegisterPageLocators.ADDRESS
    city = RegisterPageLocators.CITY
    state = RegisterPageLocators.STATE
    zip_code = RegisterPageLocators.ZIP_CODE
    phone = RegisterPageLocators.PHONE
    ssn = RegisterPageLocators.SSN
    username = RegisterPageLocators.USERNAME
    password = RegisterPageLocators.PASSWORD
    confirm_password = RegisterPageLocators.CONFIRM_PASSWORD
    register_button = RegisterPageLocators.REGISTER_BUTTON
    duplicate_username_error = RegisterPageLocators.DUPLICATE_USERNAME_ERROR
    success_title = RegisterPageLocators.SUCCESS_TITLE

    def open(self):
        self.driver.get(SYSTEM_URL)

    def register(self, user: dict):
        self.type(self.first_name, user["first_name"])
        self.type(self.last_name, user["last_name"])
        self.type(self.address, user["address"])
        self.type(self.city, user["city"])
        self.type(self.state, user["state"])
        self.type(self.zip_code, user["zip_code"])
        self.type(self.phone, user["phone"])
        self.type(self.ssn, user["ssn"])
        self.type(self.username, user["username"])
        self.type(self.password, user["password"])
        self.type(self.confirm_password, user["password"])
        self.click(self.register_button)

    def wait_for_registration_success(self):
        # register.htm re-renders in place on success (no redirect/URL change) with
        # an h1 reading "Welcome <username>" - wait for that text, not just visibility,
        # since the pre-submit page already has a visible h1.title ("Signing up is easy!")
        self.wait.until(ec.text_to_be_present_in_element(self.success_title, "Welcome"))

    def wait_for_registration_outcome(self):
        """Waits for either the duplicate-username error or a successful "Welcome"
        heading, whichever the server actually renders, and returns which one it was.

        The live demo server occasionally does not render the duplicate-username
        error on the first submit - this makes that distinguishable from a real
        locator/timing bug instead of just timing out with no information.
        """
        def _outcome(driver):
            errors = driver.find_elements(*self.duplicate_username_error)
            if errors and errors[0].is_displayed():
                return ("error", errors[0].text)
            headings = driver.find_elements(*self.success_title)
            if headings and "Welcome" in headings[0].text:
                return ("success", headings[0].text)
            return False

        return self.wait.until(_outcome)
