import logging

from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage
from pages.update_contact_page.updatecontactlocators import UpdateContactLocators
from pages.update_contact_page.updatecontactproperties import UpdateContactProperties


class UpdateContactPage(UpdateContactProperties, BasePage):
    def open(self):
        logging.info("Opening update contact page")
        self.driver.get(self.SYSTEM_URL)

        self.wait.until(EC.visibility_of_element_located(UpdateContactLocators.FIRST_NAME))

        self.wait.until(EC.text_to_be_present_in_element_value(UpdateContactLocators.LAST_NAME,"Smith"))

    def enter_text(self, field, value):
        field.clear()
        field.send_keys(value)

    def update_contact(self, first_name, last_name, address, city, state, zip_code, phone):
        logging.info("Updating contact info for %s %s", first_name, last_name)
        self.enter_text(self.first_name, first_name)
        self.enter_text(self.last_name, last_name)
        self.enter_text(self.address, address)
        self.enter_text(self.city, city)
        self.enter_text(self.state, state)
        self.enter_text(self.zip_code, zip_code)
        self.enter_text(self.phone, phone)
        self.update_button.click()

    def get_result_heading(self):
        logging.info("Waiting for update profile result heading")
        self.wait.until(EC.visibility_of_element_located(UpdateContactLocators.RESULT_TITLE))
        heading = self.result_title
        return heading.text

    def get_first_name_error(self):
        logging.info("Waiting for first name error")
        self.wait.until(EC.visibility_of_element_located(UpdateContactLocators.FIRST_NAME_ERROR))
        error = self.first_name_error
        return error.text

    def get_panel_text(self):
        panel = self.right_panel
        return panel.text

    def get_first_name_validation_message(self):
        field = self.first_name
        return field.get_attribute("validationMessage")