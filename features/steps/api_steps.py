# Directory: behave_cerberus/features/steps/api_steps.py
from behave import given, when, then
from utils.api_utils import APIUtils

@given("the API endpoint is \"{url}\"")
def step_impl(context, url):
    context.api = APIUtils()
    context.api_url = url

@when("I send a GET request")
def step_impl(context):
    context.api.send_get_request(context.api_url)

@then("the response status code should be {expected_code:d}")
def step_impl(context, expected_code):
    assert context.api.get_status_code() == expected_code

@then("the title should be \"{expected_title}\"")
def step_impl(context, expected_title):
    assert context.api.get_title() == expected_title
