# C:\Users\singh\IdeaProjects\Cerberus\pages\base_playwright_page.py

from playwright.sync_api import Page, expect
import logging

class BasePlaywrightPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate(self, url):
        """Navigates to a given URL."""
        self.logger.info(f"Navigating to URL: {url}")
        try:
            self.page.goto(url)
            self.logger.info(f"Successfully navigated to URL: {url}")
        except Exception as e:
            self.logger.error(f"Error navigating to {url}: {e}")
            raise

    def fill_field(self, selector, text):
        """Fills a text field identified by selector."""
        self.logger.info(f"Filling field '{selector}' with text: '{text}'")
        try:
            self.page.fill(selector, text)
        except Exception as e:
            self.logger.error(f"Could not fill field '{selector}': {e}")
            raise

    def click_element(self, selector):
        """Clicks an element identified by selector."""
        self.logger.info(f"Clicking element: '{selector}'")
        try:
            self.page.click(selector)
        except Exception as e:
            self.logger.error(f"Could not click element '{selector}': {e}")
            raise

    def get_text(self, selector):
        """Gets the text content of an element."""
        self.logger.info(f"Getting text from element: '{selector}'")
        try:
            return self.page.locator(selector).text_content()
        except Exception as e:
            self.logger.error(f"Could not get text from element '{selector}': {e}")
            raise

    def wait_for_selector(self, selector, timeout=10000):
        """Waits for an element identified by selector to be visible."""
        self.logger.info(f"Waiting for selector: '{selector}' to be visible.")
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=timeout)
            self.logger.info(f"Selector '{selector}' is visible.")
        except Exception as e:
            self.logger.warning(f"Timeout: Selector '{selector}' not visible after {timeout/1000} seconds.")
            raise

    def assert_text_present(self, selector, expected_text):
        """Asserts that an element contains the expected text."""
        self.logger.info(f"Asserting text in '{selector}' is '{expected_text}'")
        try:
            # Playwright's expect handles auto-waiting for text to appear
            expect(self.page.locator(selector)).to_have_text(expected_text)
            self.logger.info(f"Text '{expected_text}' found in '{selector}'.")
        except AssertionError as e:
            self.logger.error(f"Assertion Failed: Text in '{selector}' was not '{expected_text}'. Error: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Error checking text for '{selector}': {e}")
            raise

    def get_current_url(self):
        """Returns the current URL."""
        return self.page.url

    def assert_url_contains(self, expected_part):
        """Asserts that the current URL contains a specific string."""
        current_url = self.get_current_url()
        self.logger.info(f"Asserting URL '{current_url}' contains '{expected_part}'")
        if expected_part not in current_url:
            self.logger.error(f"Assertion Failed: URL '{current_url}' does not contain '{expected_part}'.")
            raise AssertionError(f"URL did not contain '{expected_part}'. Current URL: {current_url}")
        self.logger.info(f"URL '{current_url}' successfully contains '{expected_part}'.")