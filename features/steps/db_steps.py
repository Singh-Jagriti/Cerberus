# C:\Users\singh\PycharmProjects\Cerberus\features\steps\db_steps.py

from behave import given, when, then
import logging

db_logger = logging.getLogger('BehaveFramework.db_steps')

@given('a test database "{db_name}"')
def step_impl(context, db_name):
    """
    Ensures the DBUtils is connected to the specified database.
    (Connection is handled in environment.py, this step primarily serves
    to ensure context.db is available and logs the current database name.)
    """
    assert context.db.db_name == db_name, \
        f"Expected to be connected to {db_name}, but connected to {context.db.db_name}"
    db_logger.info(f"Using test database: {db_name}")

@when('I query for user with id {user_id:d}')
def step_impl(context, user_id):
    """
    Queries the database for a user by their ID and stores the result.
    """
    context.user_data = context.db.get_user_by_id(user_id)
    db_logger.info(f"Queried for user with ID: {user_id}")
    assert context.user_data is not None, f"No user found with ID {user_id}"

@then('the user name should be "{expected_name}"')
def step_impl(context, expected_name):
    """
    Validates the full name of the queried user.
    Assumes user_data is a tuple where full_name is the 4th element (index 3).
    (id, username, email, full_name)
    """
    actual_name = context.user_data[3] # Assuming full_name is at index 3
    assert actual_name == expected_name, \
        f"Expected user name '{expected_name}', but got '{actual_name}'"
    db_logger.info(f"User name validated: {actual_name}")