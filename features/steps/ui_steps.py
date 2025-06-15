# Directory: behave_cerberus/features/steps/ui_steps.py
from behave import given, when, then
from utils.browser_utils import BrowserUtils

@given("I open the demo form page")
def step_impl(context):
    context.browser = BrowserUtils()
    context.browser.open_url("https://demoqa.com/text-box")

@when("I fill the form with valid data")
def step_impl(context):
    context.browser.fill_form("Jagriti Singh", "jagriti@example.com", "123 Maple Street", "456 Oak Avenue")

@when("I submit the form")
def step_impl(context):
    context.browser.submit_form()

@then("I should see the confirmation with my name")
def step_impl(context):
    confirmation = context.browser.get_confirmation_name()
    assert "Jagriti Singh" in confirmation
    context.browser.close()