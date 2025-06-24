# C:\Users\singh\IdeaProjects\Cerberus\utils\playwright_utils.py

from playwright.sync_api import sync_playwright, Page, Browser
import logging

class PlaywrightBrowserUtils:
    def __init__(self):
        self.playwright_context = None
        self.browser = None
        self.page = None
        self.logger = logging.getLogger(self.__class__.__name__)

    def initialize_browser(self, browser_name="chromium", headless=True):
        """Initializes a Playwright browser instance."""
        self.playwright_context = sync_playwright().start()
        try:
            if browser_name.lower() == "chromium":
                self.browser = self.playwright_context.chromium.launch(headless=headless)
            elif browser_name.lower() == "firefox":
                self.browser = self.playwright_context.firefox.launch(headless=headless)
            elif browser_name.lower() == "webkit":
                self.browser = self.playwright_context.webkit.launch(headless=headless)
            else:
                raise ValueError(f"Unsupported browser: {browser_name}. Choose from 'chromium', 'firefox', 'webkit'.")

            self.page = self.browser.new_page()
            self.logger.info(f"Playwright {browser_name.capitalize()} browser initialized successfully.")
        except Exception as e:
            self.logger.error(f"Error initializing Playwright browser: {e}")
            raise

    def close_browser(self):
        """Closes the Playwright browser."""
        if self.browser:
            self.browser.close()
            self.logger.info("Playwright browser closed successfully.")
        if self.playwright_context:
            self.playwright_context.stop()
            self.logger.info("Playwright context stopped.")
        self.browser = None
        self.page = None

    def get_page(self) -> Page:
        """Returns the Playwright Page object."""
        if not self.page:
            raise RuntimeError("Playwright page not initialized. Call initialize_browser first.")
        return self.page