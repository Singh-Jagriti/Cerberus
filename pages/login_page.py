
# Temporary comment for Git test
# C:\Users\singh\PycharmProjects\Cerberus\pages\login_page.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
import logging


class LoginPage(BasePage):
    BASE_UI_URL = "https://demoqa.com"
    URL = "https://demoqa.com/login" # Initial login page URL
    PROFILE_URL_PART = "/profile" # Part of the URL after successful login

    USERNAME_FIELD = (By.ID, "userName")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    # LOGOUT_BUTTON and related method are removed as per your suggestion
    # LOADING_SPINNER is optional, keep only if it actually exists and is problematic
    LOADING_SPINNER = (By.ID, "loading-indicator") # You may remove this if no spinner is visible

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    def load(self):
        self.open_url(self.URL)
        self.logger.info(f"Navigated to Login Page: {self.URL}")

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
        self.logger.info("Login button clicked.")
        # After clicking login, implicitly wait for the URL to change in the step definition

    # Keep wait_for_loading_to_disappear only if a spinner is genuinely present and causes issues
    def wait_for_loading_to_disappear(self, timeout=15):
        self.logger.info("Waiting for loading indicator to disappear.")
        try:
            self.wait_until_element_is_invisible(self.LOADING_SPINNER, timeout)
            self.logger.info("Loading indicator disappeared.")
        except TimeoutException:
            self.logger.debug("Loading indicator did not disappear in time or was not found, proceeding...")


    # Helper method (ensure this is in BasePage or here if not)
    def wait_until_element_is_invisible(self, by_locator, timeout=None):
        wait_time = timeout if timeout is not None else self.wait._timeout
        try:
            WebDriverWait(self.driver, wait_time).until(EC.invisibility_of_element_located(by_locator))
            self.logger.debug(f"Element {by_locator} is now invisible.")
        except TimeoutException:
            self.logger.warning(f"Timeout: Element {by_locator} did not become invisible after {wait_time} seconds.")
            raise