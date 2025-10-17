Feature: Add item to Target cart

  Scenario: Add item to cart and verify it is added
    Given User is on target home page
    When user search item
    And user adds item to the cart
    Then user should see item in the cart
