from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


# 2. Create a test case using BDD that
# opens target.com, (given)
# clicks on the cart icon (when)
# and verifies that “Your cart is empty” message is shown: (then)


@when("Click on Cart icon")
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    # context.app.main_page.open()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
