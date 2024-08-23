Feature: Verify users can navigate to sign in page from main page
    Scenario: verify that a logged-out user can navigate to Sign In Page
        Given Open target main page
        When click Sign In
        Then Verify Sign In form opened
