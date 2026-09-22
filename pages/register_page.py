from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage

SYSTEM_URL = "https://parabank.parasoft.com/parabank/register.htm"


class RegisterPage(BasePage):
    first_name = (By.ID, "customer.firstName")
    last_name = (By.ID, "customer.lastName")
    address = (By.ID, "customer.address.street")
    city = (By.ID, "customer.address.city")
    state = (By.ID, "customer.address.state")
    zip_code = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    ssn = (By.ID, "customer.ssn")
    username = (By.ID, "customer.username")
    password = (By.ID, "customer.password")
    confirm_password = (By.ID, "repeatedPassword")
    register_button = (By.XPATH, "//input[@value='Register']")
    duplicate_username_error = (By.ID, "customer.username.errors")
    success_title = (By.CSS_SELECTOR, "#rightPanel h1.title")

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
