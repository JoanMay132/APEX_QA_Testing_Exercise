Feature: Liverpool search bar
  As a consumer
  I want to easily search for different types of articles
  So that I can find articles of my interest

  Scenario Outline: Check search results with different inputs
    Given I launch the browser
    When I open the Liverpool homepage
    And I click the search bar
    And I type "<search_term>" in the search bar
    And I click on the search button
    Then I should see "<expected_results>"
    And I close the browser
    
    Examples:
      | search_term                   | expected_results                    |
      | toys                          | list of articles related to toys     |
      | wh3el                         | message indicating no articles found |
      | NO_SPACE                      | same page                            |
      | TRIPLE_SPACE                  | current page                         |
      | Samsung Galaxy S21 5G         | list of articles related to Samsung Galaxy S21 5G |
      | Electronics                   | list of articles related to the Electronics category |
