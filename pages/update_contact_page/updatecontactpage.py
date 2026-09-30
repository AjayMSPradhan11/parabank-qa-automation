import logging

from selenium.webdriver.support import expected_conditions as ec

from pages.basepage import BasePage
from pages.update_contact_page.updatecontactlocators import UpdatecontactLocators
from pages.update_contact_page.updatecontactproperties import UpdatecontactProperties


class UpdatecontactPage(UpdatecontactProperties, BasePage):
    def open(self):
        logging.info("Opening update contact page")
        self.driver.get(self.SYSTEM_URL)

        self.wait.until(ec.visibility_of_element_located(UpdatecontactLocators.FIRST_NAME))

        self.wait.until(ec.text_to_be_present_in_element_value(UpdatecontactLocators.LAST_NAME,"Smith"))

    def enter_text(self, field, value):
        field.clear()
        field.send_keys(value)

    def update_contact(self, contact):
        logging.info("Updating contact info for %s %s", contact["first_name"], contact["last_name"])
        self.enter_text(self.first_name, contact["first_name"])
        self.enter_text(self.last_name, contact["last_name"])
        self.enter_text(self.address, contact["address"])
        self.enter_text(self.city, contact["city"])
        self.enter_text(self.state, contact["state"])
        self.enter_text(self.zip_code, contact["zip_code"])
        self.enter_text(self.phone, contact["phone"])
        self.update_button.click()

    def get_result_heading(self):
        logging.info("Waiting for update profile result heading")
        self.wait.until(ec.visibility_of_element_located(UpdatecontactLocators.RESULT_TITLE))
        heading = self.result_title
        return heading.text

    def get_first_name_error(self):
        logging.info("Waiting for first name error")
        self.wait.until(ec.visibility_of_element_located(UpdatecontactLocators.FIRST_NAME_ERROR))
        error = self.first_name_error
        return error.text

    def get_panel_text(self):
        panel = self.right_panel
        return panel.text

    def get_first_name_validation_message(self):
        field = self.first_name
        return field.get_attribute("validationMessage")