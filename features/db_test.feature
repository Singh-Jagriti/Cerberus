# C:\Users\singh\PycharmProjects\Cerberus\features\db_test.feature

Feature: Validate data in database
  As a system administrator
  I want to verify data integrity in the database

  Scenario: Check if user exists in the database
    Given a test database "test_users.db"
    When I query for user with id 1
    Then the user name should be "Jagriti Singh"