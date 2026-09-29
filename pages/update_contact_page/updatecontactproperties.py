from pages.update_contact_page.updatecontactlocators import UpdateContactLocators


class UpdateContactProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/updateprofile.htm"

    @property
    def first_name(self):
        return self.driver.find_element(*UpdateContactLocators.FIRST_NAME)

    @property
    def last_name(self):
        return self.driver.find_element(*UpdateContactLocators.LAST_NAME)

    @property
    def address(self):
        return self.driver.find_element(*UpdateContactLocators.ADDRESS)

    @property
    def city(self):
        return self.driver.find_element(*UpdateContactLocators.CITY)

    @property
    def state(self):
        return self.driver.find_element(*UpdateContactLocators.STATE)

    @property
    def zip_code(self):
        return self.driver.find_element(*UpdateContactLocators.ZIP_CODE)

    @property
    def phone(self):
        return self.driver.find_element(*UpdateContactLocators.PHONE)

    @property
    def update_button(self):
        return self.driver.find_element(*UpdateContactLocators.UPDATE_BUTTON)

    @property
    def right_panel(self):
        return self.driver.find_element(*UpdateContactLocators.RIGHT_PANEL)

    @property
    def result_title(self):
        return self.driver.find_element(*UpdateContactLocators.RESULT_TITLE)

    @property
    def first_name_error(self):
        return self.driver.find_element(*UpdateContactLocators.FIRST_NAME_ERROR)