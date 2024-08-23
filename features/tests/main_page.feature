Feature: Tests for main page UI

  Scenario: Verify header is shown
    Given Open target main page
    Then Verify header is shown

  Scenario: Verify header has correct amount links
    Given Open target main page
    Then Verify header has 6 links
