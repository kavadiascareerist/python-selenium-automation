# Created by mwunguramugabe at 10/15/25
Feature: Verifying target cart is empty
  Scenario: User is able to see "your cart is empty" message
    Given User is on target home page
    When User clicks on cart button
    Then User sees a message " your cart is empty"



