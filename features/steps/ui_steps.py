# C:\Users\singh\PycharmProjects\Cerberus\features\steps\ui_steps.py

from behave import given, when, then
import logging
from selenium.webdriver.common.by import By # If specific locators are used directly here, although better in page object

ui_logger = logging.getLogger('BehaveFramework.ui_steps')

@given('I open the demo form page')
def step_impl(context):
    """
    Opens the specific demo form page for the UI test.
    This uses a different URL than the login page.
    """
    # Assuming context.browser has methods like open_url or you use a page object
    # For this specific scenario, let's open the text-box page.
    # We can either make a dedicated page object for text-box or open it directly.
    # Let's open it directly for simplicity, assuming context.browser is BrowserUtils
    # And BrowserUtils has a self.driver for opening.
    url = f"{context.login_page.BASE_UI_URL}/text-box" # Reusing BASE_UI_URL from LoginPage
    context.browser.driver.get(url) # Using context.browser.driver directly
    ui_logger.info(f"Opened URL: {url}")


@when('I fill the form with valid data')
def step_impl(context):
    """
    Fills the text box form fields.
    Using specific IDs for DemoQA's Text Box form.
    """
    # Assuming BrowserUtils handles entering text and scrolling
    # In a real scenario, this would ideally be done via a dedicated Page Object for this form.
    # For now, let's use context.browser.enter_text, assuming it exists or can be adapted.
    # Or, given our BasePage now has enter_text and click_element, we can directly use driver.find_element and then send_keys/click
    # Let's use the BasePage methods via a temporary instance or by adding a dedicated FormPage.

    # Option 1: Using the driver directly with BasePage methods (less ideal for maintainability)
    # This requires recreating BasePage or accessing its methods differently.
    # Better: If you had a dedicated 'TextBoxFormPage' page object, you'd use that.
    # For now, let's simulate filling using direct calls but leveraging BasePage's robustness.
    # Note: The BasePage is accessed via context.login_page because it's the only page object
    # we've initialized in environment.py so far. This is not ideal for multiple pages,
    # but works for demonstrating the features of BasePage.

    context.login_page.enter_text((By.ID, "userName"), "Jagriti Singh")
    context.login_page.enter_text((By.ID, "userEmail"), "jagriti@example.com")
    context.login_page.enter_text((By.ID, "currentAddress"), "123 Maple Street")
    context.login_page.enter_text((By.ID, "permanentAddress"), "456 Oak Avenue")
    ui_logger.info("Form fields filled.")

@when('I submit the form')
def step_impl(context):
    """
    Clicks the submit button on the form.
    """
    context.login_page.click_element((By.ID, "submit"))
    ui_logger.info("Submit button clicked.")

@then('I should see the confirmation with my name')
def step_impl(context):
    """
    Verifies that the confirmation message contains the entered name.
    """
    # The confirmation text appears in a div with id="output"
    # and the name is specifically in a p tag like <p id="name">Name:Jagriti Singh</p>
    confirmation_name_locator = (By.ID, "name")
    actual_name_text = context.login_page.get_element_text(confirmation_name_locator)
    ui_logger.info(f"Retrieved confirmation name: '{actual_name_text}'")
    assert "Name:Jagriti Singh" in actual_name_text, \
        f"Expected confirmation to contain 'Name:Jagriti Singh', but got '{actual_name_text}'"