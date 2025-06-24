# C:\Users\singh\IdeaProjects\Cerberus\pages\playwright_form_page.py

from pages.base_playwright_page import BasePlaywrightPage
from playwright.sync_api import Page
import logging

class PlaywrightFormPage(BasePlaywrightPage):
    URL = "https://demoqa.com/text-box"

    # Locators (using Playwright's preferred CSS selectors for simplicity)
    FULL_NAME_FIELD = "#userName"
    EMAIL_FIELD = "#userEmail"
    CURRENT_ADDRESS_FIELD = "#currentAddress"
    PERMANENT_ADDRESS_FIELD = "#permanentAddress"
    SUBMIT_BUTTON = "#submit"
    OUTPUT_NAME = "#output #name"
    OUTPUT_EMAIL = "#output #email"
    OUTPUT_CURRENT_ADDRESS = "#output #currentAddress"
    OUTPUT_PERMANENT_ADDRESS = "#output #permanentAddress"

    def __init__(self, page: Page):
        super().__init__(page)
        self.logger = logging.getLogger(self.__class__.__name__)

    def load(self):
        self.navigate(self.URL)
        self.logger.info(f"Opened Playwright demo form page: {self.URL}")

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.logger.info("Filling form with data using Playwright.")
        self.fill_field(self.FULL_NAME_FIELD, full_name)
        self.fill_field(self.EMAIL_FIELD, email)
        self.fill_field(self.CURRENT_ADDRESS_FIELD, current_address)
        self.fill_field(self.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.logger.info("Playwright form fields filled.")

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)
        self.logger.info("Playwright submit button clicked.")

    def get_output_name(self):
        return self.get_text(self.OUTPUT_NAME)

    def get_output_email(self):
        return self.get_text(self.OUTPUT_EMAIL)

    def get_output_current_address(self):
        return self.get_text(self.OUTPUT_CURRENT_ADDRESS)

    def get_output_permanent_address(self):
        return self.get_text(self.OUTPUT_PERMANENT_ADDRESS)