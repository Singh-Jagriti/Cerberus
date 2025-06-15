Feature: API GET request validation

  Scenario: Validate JSONPlaceholder GET response
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request
    Then the response status code should be 200
    And the title should be "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
