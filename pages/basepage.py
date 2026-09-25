import logging

from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 15

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        logger.info("Initializing page object")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
