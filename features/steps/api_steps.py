# C:\Users\singh\PycharmProjects\Cerberus\features\steps\api_steps.py

from behave import given, when, then
import logging

api_logger = logging.getLogger('BehaveFramework.api_steps')

@given('the API endpoint is "{endpoint}"')
def step_impl(context, endpoint):
    """
    Sets the API endpoint for the current scenario.
    The base_url is configured in environment.py.
    """
    context.api_endpoint = endpoint
    api_logger.info(f"API endpoint set to: {context.api.base_url}{context.api_endpoint}")

@when('I send a GET request')
def step_impl(context):
    """
    Sends a GET request to the set API endpoint.
    """
    context.response = context.api.get(context.api_endpoint)
    api_logger.info("GET request sent.")

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    """
    Validates the HTTP response status code.
    """
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, but got {context.response.status_code}"

@then('the title should be "{expected_title}"')
def step_impl(context, expected_title):
    """
    Validates a specific field (e.g., 'title') in the JSON response.
    """
    response_json = context.response.json()
    actual_title = response_json.get('title')
    assert actual_title == expected_title, \
        f"Expected title '{expected_title}', but got '{actual_title}'"