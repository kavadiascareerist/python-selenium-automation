
Feature: Verify user can navigate to sign-in button

  Scenario: User can see the sign-in button when logged out
    Given User is on target home page
    When User is logged out
    Then User sees the sign-in button
