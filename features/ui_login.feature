# features/ui_login.feature

Feature: User Login and Logout Functionality
  As a registered user
  I want to log in to the web application
  So that I can access my profile and log out

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username and password
    And I click the login button
    Then the URL should be the profile page