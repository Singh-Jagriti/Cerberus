# C:\Users\singh\PycharmProjects\Cerberus\features\steps\ui_login_steps.py

from behave import given, when, then
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait # Import WebDriverWait for URL check

context_logger = logging.getLogger('BehaveFramework.ui_login_steps')

@given('I am on the login page')
def step_impl(context):
    context.login_page.load()
    context_logger.info(f"Navigated to the login page: {context.login_page.URL}")

@when('I enter valid username and password')
def step_impl(context):
    context.username = "testuser"
    context.password = "Password123!"

    context.login_page.login(context.username, context.password)
    context_logger.info(f"Attempted login with username: {context.username}")

@when('I click the login button')
def step_impl(context):
    context_logger.info("Login button click handled by previous step (enter valid username and password).")
    pass

@then('the URL should be the profile page')
def step_impl(context):
    expected_url_part = context.login_page.PROFILE_URL_PART # This is "/profile"
    current_url = context.driver.current_url # Initial URL before wait

    # Use WebDriverWait to wait for the URL to contain the profile part
    try:
        WebDriverWait(context.driver, 15).until(
            EC.url_contains(expected_url_part)
        )
        current_url = context.driver.current_url # Get the final URL after wait
        context_logger.info(f"URL successfully changed to profile page: {current_url}")
    except TimeoutException:
        context_logger.error(f"Timeout: URL did not change to profile page. Current URL: {current_url}")
        raise AssertionError(f"URL did not change to profile page. Expected to contain '{expected_url_part}', but found '{current_url}'")