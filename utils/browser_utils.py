# C:\Users\singh\PycharmProjects\Cerberus\utils\browser_utils.py

import logging

class BrowserUtils:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Chrome WebDriver initialized successfully.")

    def close_browser(self):
        """Closes the browser."""
        if self.driver:
            self.driver.quit()
            self.logger.info("Browser closed successfully.")

    def take_screenshot(self, file_path):
        """Takes a screenshot and saves it to the specified path."""
        try:
            self.driver.save_screenshot(file_path)
            self.logger.info(f"Screenshot saved to: {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to take screenshot to {file_path}: {e}")
            return False

    # Note: Scrolling methods previously discussed are now moved to BasePage
    # because they are element-specific interactions that Page Objects will use.
    # BrowserUtils can remain for broader browser actions like opening, closing, screenshotting.