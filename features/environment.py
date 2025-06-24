# C:\Users\singh\PycharmProjects\Cerberus\features\environment.py

import os
import logging
from behave import *
from behave.model import Status
from selenium import webdriver # For Selenium
from utils.browser_utils import BrowserUtils # For Selenium
from pages.login_page import LoginPage # For Selenium UI page objects


# New Playwright Imports
from utils.playwright_utils import PlaywrightBrowserUtils
from pages.playwright_form_page import PlaywrightFormPage


from utils.db_utils import DBUtils
from utils.api_utils import APIUtils


# Configure logging for the entire framework
logging.basicConfig(level=logging.INFO,  # Set the minimum level to log
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Get a logger specific to the Behave framework
framework_logger = logging.getLogger('BehaveFramework')

def before_all(context):
    """
    Setup for the entire test run.
    Initializes browser, database, and API clients.
    """
    framework_logger.info("--- Test Run Started ---")

    # --- Initialize Utility Classes (but don't launch browsers yet) ---
    framework_logger.info("Initializing Browser Utilities...")
    context.browser_utils = BrowserUtils(None) # Initialize without a driver yet for Selenium
    context.playwright_browser_utils = PlaywrightBrowserUtils() # Initialize Playwright utility
    framework_logger.info("Browser Utilities initialized.")

    # --- Database Setup ---
    framework_logger.info("Initializing Database...")
    context.db = DBUtils('test_users.db') # Example database file
    context.db.create_users_table() # Ensure table exists and add dummy data
    framework_logger.info("Database initialized and tables ensured.")

    # --- API Client Setup ---
    framework_logger.info("Initializing API client...")
    # Example base URL for a public API
    context.api = APIUtils(base_url=os.getenv("BASE_API_URL", "https://jsonplaceholder.typicode.com"))
    framework_logger.info(f"API client initialized with base URL: {context.api.base_url}.")

    framework_logger.info("Page Objects initialized.") # This log line can be moved here
    # Page objects are now initialized in before_scenario based on browser type


def after_all(context):
    """
    Teardown for the entire test run.
    Closes browser, database, and performs cleanup.
    """
    framework_logger.info("--- Test Run Finished ---")

    # --- Browser Teardown (ensure all browser instances are closed) ---
    # Selenium cleanup (if a driver was initialized and still active)
    if hasattr(context, 'driver') and context.driver:
        try:
            context.driver.quit()
            framework_logger.info("Selenium browser closed.")
        except Exception as e:
            framework_logger.warning(f"Error closing Selenium browser in after_all: {e}")

    # Playwright cleanup (if a browser was initialized and still active)
    if hasattr(context, 'playwright_browser_utils') and context.playwright_browser_utils.browser:
        try:
            context.playwright_browser_utils.close_browser()
            framework_logger.info("Playwright browser closed via after_all.")
        except Exception as e:
            framework_logger.warning(f"Error closing Playwright browser in after_all: {e}")


    # --- Database Teardown ---
    if hasattr(context, 'db') and context.db:
        context.db.close_connection()
        framework_logger.info(f"Database connection to {context.db.db_name} closed.")

    framework_logger.info("Browser closed.") # Consolidate log

def before_feature(context, feature):
    """
    Setup before each feature runs.
    """
    framework_logger.info(f"--- Starting Feature: {feature.name} ---")

def after_feature(context, feature):
    """
    Teardown after each feature runs.
    """
    framework_logger.info(f"--- Finished Feature: {feature.name} ---")

def before_scenario(context, scenario):
    """
    Setup before each scenario runs.
    Initializes browser and page objects based on scenario tags.
    """
    # Check for Playwright tag
    if 'playwright' in scenario.tags:
        framework_logger.info(f"--- Starting Playwright Scenario: {scenario.name} ---")
        context.playwright_browser_utils.initialize_browser() # Default to chromium, headless=True
        context.playwright_page = context.playwright_browser_utils.get_page() # Get Playwright Page object
        context.playwright_form_page = PlaywrightFormPage(context.playwright_page) # Initialize Playwright page object
        context.browser_type = "playwright" # Store browser type for after_scenario
    else:
        # Default to Selenium if no specific tag (or other non-playwright tags)
        framework_logger.info(f"--- Starting Selenium Scenario: {scenario.name} ---")
        context.driver = webdriver.Chrome() # Initialize Selenium driver per scenario
        context.driver.maximize_window()
        context.browser_utils.driver = context.driver # Assign the driver to the Selenium utility
        context.login_page = LoginPage(context.driver) # Initialize Selenium login page

        context.browser_type = "selenium" # Store browser type for after_scenario


def after_scenario(context, scenario):
    """
    Teardown after each scenario runs.
    Closes the specific browser used for the scenario and takes screenshot on failure.
    """
    status = "passed" if scenario.status == Status.passed else \
             "failed" if scenario.status == Status.failed else \
             "skipped"
    framework_logger.info(f"Finished Scenario: {scenario.name} - Status: {status}")

    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    scenario_name_safe = scenario.name.replace(' ', '_').replace('/', '_') # Sanitize name for file system

    # Take screenshot on failure based on the browser type used
    if scenario.status == Status.failed:
        if hasattr(context, 'browser_type') and context.browser_type == "playwright":
            if hasattr(context, 'playwright_page') and context.playwright_page:
                try:
                    screenshot_path = os.path.join(screenshot_dir, f"PW_{scenario_name_safe}_failed.png")
                    context.playwright_page.screenshot(path=screenshot_path)
                    framework_logger.info(f"Playwright Screenshot taken: {screenshot_path}")
                except Exception as e:
                    framework_logger.error(f"Error taking Playwright screenshot: {e}")
        elif hasattr(context, 'browser_type') and context.browser_type == "selenium":
            if hasattr(context, 'browser_utils') and context.browser_utils.driver:
                try:
                    screenshot_path = os.path.join(screenshot_dir, f"SE_{scenario_name_safe}_failed.png")
                    context.browser_utils.take_screenshot(screenshot_path)
                    framework_logger.info(f"Selenium Screenshot taken: {screenshot_path}")
                except Exception as e:
                    framework_logger.error(f"Error taking Selenium screenshot: {e}")


    # Close the browser specific to the scenario
    if hasattr(context, 'browser_type') and context.browser_type == "playwright":
        if hasattr(context, 'playwright_browser_utils') and context.playwright_browser_utils.browser:
            context.playwright_browser_utils.close_browser()
    elif hasattr(context, 'browser_type') and context.browser_type == "selenium":
        if hasattr(context, 'driver') and context.driver:
            try:
                context.driver.quit() # Use driver.quit() for Selenium cleanup per scenario
                framework_logger.info("Selenium browser closed after scenario.")
            except Exception as e:
                framework_logger.warning(f"Error closing Selenium browser after scenario: {e}")