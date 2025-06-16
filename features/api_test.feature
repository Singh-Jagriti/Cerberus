# C:\Users\singh\PycharmProjects\Cerberus\features\api_test.feature

Feature: API GET request validation
  As an API consumer
  I want to validate GET responses from a public API

  Scenario: Validate JSONPlaceholder GET response
    Given the API endpoint is "/posts/1"
    When I send a GET request
    Then the response status code should be 200
    And the title should be "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"