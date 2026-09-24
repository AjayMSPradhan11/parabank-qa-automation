from pages.register_page.registerlocators import RegisterLocators


class RegisterProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/register.htm"

    @property
    def first_name(self):
        return self.driver.find_element(*RegisterLocators.FIRST_NAME)

    @property
    def last_name(self):
        return self.driver.find_element(*RegisterLocators.LAST_NAME)

    @property
    def address(self):
        return self.driver.find_element(*RegisterLocators.ADDRESS)

    @property
    def city(self):
        return self.driver.find_element(*RegisterLocators.CITY)

    @property
    def state(self):
        return self.driver.find_element(*RegisterLocators.STATE)

    @property
    def zip_code(self):
        return self.driver.find_element(*RegisterLocators.ZIP_CODE)

    @property
    def phone(self):
        return self.driver.find_element(*RegisterLocators.PHONE)

    @property
    def ssn(self):
        return self.driver.find_element(*RegisterLocators.SSN)

    @property
    def username(self):
        return self.driver.find_element(*RegisterLocators.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*RegisterLocators.PASSWORD)

    @property
    def confirm_password(self):
        return self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD)

    @property
    def register_button(self):
        return self.driver.find_element(*RegisterLocators.REGISTER_BUTTON)

    @property
    def duplicate_username_error(self):
        return self.driver.find_element(*RegisterLocators.DUPLICATE_USERNAME_ERROR)

    @property
    def success_title(self):
        return self.driver.find_element(*RegisterLocators.SUCCESS_TITLE)
