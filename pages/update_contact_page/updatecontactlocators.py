from selenium.webdriver.common.by import By


class UpdatecontactLocators:
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "input[value='Update Profile']")
    RESULT_TITLE = (By.XPATH, "//h1[contains(text(), 'Profile Updated')]")
    FIRST_NAME_ERROR = (By.ID,"firstName-error")