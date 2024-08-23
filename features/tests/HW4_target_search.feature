# Created by ilarievilbrun at 8/12/24, for 'target_search_steps.py'
Feature: Target main page search tests
  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product_outcome>
    And Verify correct search results URL opens for <product_outcome>
    Examples:
    |product  |product_outcome    |
    |milk     |milk               |
    |juice    |juice              |
    |soda     |soda               |
    |coffee   |coffee             |
    |tea      |tea                |
    |water    |water              |


