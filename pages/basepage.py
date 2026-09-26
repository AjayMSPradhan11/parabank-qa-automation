import logging

from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 15


class BasePage:
    def __init__(self, driver):
        logging.info("Initializing page object")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
