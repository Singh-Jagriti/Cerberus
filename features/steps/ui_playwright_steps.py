# C:\Users\singh\IdeaProjects\Cerberus\features\steps\ui_playwright_steps.py

from behave import given, when, then
import logging
from pages.playwright_form_page import PlaywrightFormPage

context_logger = logging.getLogger('BehaveFramework.ui_playwright_steps')

@given('I open the Playwright demo form page')
def step_impl(context):
    context.playwright_form_page.load()
    context_logger.info(f"Opened Playwright demo form page: {context.playwright_form_page.URL}")

@when('I fill the Playwright form with valid data')
def step_impl(context):
    context.playwright_form_page.fill_form(
        "Playwright User",
        "playwright.user@example.com",
        "789 Playwright Lane",
        "101 Playwright Blvd"
    )
    context_logger.info("Playwright form fields filled.")

@when('I submit the Playwright form')
def step_impl(context):
    context.playwright_form_page.submit_form()
    context_logger.info("Playwright submit button clicked.")

@then('I should see the Playwright confirmation with my name')
def step_impl(context):
    confirmed_name = context.playwright_form_page.get_output_name()
    expected_name_prefix = "Name:"
    expected_full_name = "Playwright User"

    context_logger.info(f"Retrieved Playwright confirmation name: '{confirmed_name}'")

    assert confirmed_name.startswith(expected_name_prefix), \
        f"Expected confirmation name to start with '{expected_name_prefix}', but got '{confirmed_name}'"
    assert expected_full_name in confirmed_name, \
        f"Expected confirmation name to contain '{expected_full_name}', but got '{confirmed_name}'"
    context_logger.info(f"Playwright confirmation name validated: '{confirmed_name}'")