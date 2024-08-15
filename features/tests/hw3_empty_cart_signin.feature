Feature: Tests for Empty Cart Functionality & Sign In Page (HW3)

Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

Scenario: verify that a logged-out user can navigate to Sign In
    Given Open Target main page
    When click Sign In
    Then Verify Sign In form opened

