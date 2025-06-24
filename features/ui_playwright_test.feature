# features/ui_playwright_test.feature

Feature: Web UI form submission with Playwright
  As a user
  I want to fill out a form using Playwright
  So that I can submit my information and confirm it with Playwright
@playwright
  Scenario: Fill and submit a form using Playwright
    Given I open the Playwright demo form page
    When I fill the Playwright form with valid data
    And I submit the Playwright form
    Then I should see the Playwright confirmation with my name