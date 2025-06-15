# Directory: behave_cerberus/features/steps/db_steps.py
from behave import given, when, then
from utils.db_utils import DBUtils

@given("a test database \"{db_name}\"")
def step_impl(context, db_name):
    context.db = DBUtils(db_name)

@when("I query for user with id {user_id:d}")
def step_impl(context, user_id):
    context.user_name = context.db.fetch_user_by_id(user_id)

@then("the user name should be \"{expected_name}\"")
def step_impl(context, expected_name):
    assert context.user_name == expected_name
    context.db.close()