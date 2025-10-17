Feature: Test Scenarios for Search functionality

  Scenario: User can search for tea
    Given Open Target page home page
    When Input tea into search button
    And Click on search icon
    Then tea is displayed in search box