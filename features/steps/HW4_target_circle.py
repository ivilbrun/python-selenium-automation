from selenium.webdriver.common.by import By
from behave import given, then


# # 2. Create a test case that will
# # open the Target Circle page https://www.target.com/circle,
# # and verify there are 10 benefit cells:

BENEFIT_BOXES = (By.CSS_SELECTOR, 'div[data-component="Cells Component Container"] div[class="cell-item-content"]')


@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify URL has 10 benefit cells')
def benefit_circle(context):
    benefit_boxes_len = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes_len) == 10, f'Expected 10 benefit cells, got {len(benefit_boxes_len)}'