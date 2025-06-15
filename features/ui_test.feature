Feature: Web UI form submission

  Scenario: Fill and submit a form
    Given I open the demo form page
    When I fill the form with valid data
    And I submit the form
    Then I should see the confirmation with my name
