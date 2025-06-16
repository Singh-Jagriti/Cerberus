# C:\Users\singh\PycharmProjects\Cerberus\pages\base_page.py

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException, ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, wait_time=15):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)
        self.logger = logging.getLogger(self.__class__.__name__)

    def open_url(self, url):
        self.logger.info(f"Opening URL: {url}")
        try:
            self.driver.get(url)
            self.logger.info(f"Successfully opened URL: {url}")
        except WebDriverException as e:
            self.logger.error(f"Failed to open URL {url}: {e}")
            raise

    def scroll_to_view(self, by_locator, timeout=None):
        wait_time = timeout if timeout is not None else self.wait._timeout
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.logger.debug(f"Scrolled to element: {by_locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not present for scrolling after {wait_time} seconds: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(f"Error scrolling to element {by_locator}: {e}")
            raise

    def find_element(self, by_locator, timeout=None):
        wait_time = timeout if timeout is not None else self.wait._timeout
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(by_locator))
            self.logger.debug(f"Element found: {by_locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Timeout: Element not present after {wait_time} seconds: {by_locator}")
            raise
        except NoSuchElementException:
            self.logger.error(f"NoSuchElement: Element not found: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(f"Error finding element {by_locator}: {e}")
            raise

    def click_element(self, by_locator, timeout=None):
        wait_time = timeout if timeout is not None else self.wait._timeout
        try:
            self.scroll_to_view(by_locator, timeout)
            element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator))
            try:
                element.click()
                self.logger.info(f"Clicked element: {by_locator}")
            except ElementClickInterceptedException:
                self.logger.warning(f"Element click intercepted for {by_locator}. Attempting JavaScript click.")
                self.driver.execute_script("arguments[0].click();", element)
                self.logger.info(f"JavaScript clicked element: {by_locator}")
            except WebDriverException as e:
                self.logger.error(f"WebDriver error clicking {by_locator}: {e}. Attempting JavaScript click as fallback.")
                self.driver.execute_script("arguments[0].click();", element)
                self.logger.info(f"JavaScript clicked element (fallback): {by_locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable after {wait_time} seconds: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(f"Error clicking element {by_locator}: {e}")
            raise

    def enter_text(self, by_locator, text, timeout=None):
        wait_time = timeout if timeout is not None else self.wait._timeout
        try:
            self.scroll_to_view(by_locator, timeout)
            element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' into {by_locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not visible after {wait_time} seconds for text entry: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(f"Error entering text into {by_locator}: {e}")
            raise

    def get_element_text(self, by_locator, timeout=None):
        """Gets text from an element using explicit wait for visibility."""
        wait_time = timeout if timeout is not None else self.wait._timeout
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
            self.logger.debug(f"Retrieved text from {by_locator}")
            return element.text
        except TimeoutException:
            self.logger.error(f"Timeout: Element text not visible after {wait_time} seconds: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(f"Error getting text from element {by_locator}: {e}")
            raise

    def wait_for_text_in_element(self, by_locator, expected_text, timeout=None):
        """
        Waits for an element to contain specific text.
        Returns the element's text if found, raises TimeoutException otherwise.
        """
        wait_time = timeout if timeout is not None else self.wait._timeout
        self.logger.info(f"Waiting for text '{expected_text}' in element {by_locator}")
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.text_to_be_present_in_element(by_locator, expected_text)
            )
            # Once text is present, get the full text of the element
            element = self.find_element(by_locator)
            actual_text = element.text
            self.logger.info(f"Found expected text in {by_locator}. Actual text: '{actual_text}'")
            return actual_text
        except TimeoutException:
            # Try to get the current text of the element to provide more context in the error
            current_text = "Element not found or no text"
            try:
                element = self.find_element(by_locator, timeout=1) # Quick check for presence
                current_text = element.text
            except (TimeoutException, NoSuchElementException):
                pass # Element not even present
            self.logger.error(f"Timeout: Text '{expected_text}' not found in element {by_locator} "
                              f"after {wait_time} seconds. Current text: '{current_text}'")
            raise
        except Exception as e:
            self.logger.error(f"Error waiting for text in element {by_locator}: {e}")
            raise