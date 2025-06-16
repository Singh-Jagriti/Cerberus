# C:\Users\singh\PycharmProjects\Cerberus\features\ui_test.feature

Feature: Web UI form submission
  As a user
  I want to fill out a form
  So that I can submit my information

  Scenario: Fill and submit a form
    Given I open the demo form page
    When I fill the form with valid data
    And I submit the form
    Then I should see the confirmation with my name