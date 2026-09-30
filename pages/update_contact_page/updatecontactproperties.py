from pages.update_contact_page.updatecontactlocators import UpdatecontactLocators


class UpdatecontactProperties:
    SYSTEM_URL = "https://parabank.parasoft.com/parabank/updateprofile.htm"

    @property
    def first_name(self):
        return self.driver.find_element(*UpdatecontactLocators.FIRST_NAME)

    @property
    def last_name(self):
        return self.driver.find_element(*UpdatecontactLocators.LAST_NAME)

    @property
    def address(self):
        return self.driver.find_element(*UpdatecontactLocators.ADDRESS)

    @property
    def city(self):
        return self.driver.find_element(*UpdatecontactLocators.CITY)

    @property
    def state(self):
        return self.driver.find_element(*UpdatecontactLocators.STATE)

    @property
    def zip_code(self):
        return self.driver.find_element(*UpdatecontactLocators.ZIP_CODE)

    @property
    def phone(self):
        return self.driver.find_element(*UpdatecontactLocators.PHONE)

    @property
    def update_button(self):
        return self.driver.find_element(*UpdatecontactLocators.UPDATE_BUTTON)

    @property
    def right_panel(self):
        return self.driver.find_element(*UpdatecontactLocators.RIGHT_PANEL)

    @property
    def result_title(self):
        return self.driver.find_element(*UpdatecontactLocators.RESULT_TITLE)

    @property
    def first_name_error(self):
        return self.driver.find_element(*UpdatecontactLocators.FIRST_NAME_ERROR)