Feature: Test Scenarios for Search functionality

  Scenario: User can search for tea
    Given user open Target home page
    When put tea into search button
    And Click on search icon
    Then tea is in search box