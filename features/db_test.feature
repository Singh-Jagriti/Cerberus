Feature: Validate data in database

  Scenario: Check if user exists in the database
    Given a test database "test_users.db"
    When I query for user with id 1
    Then the user name should be "Jagriti Singh"
