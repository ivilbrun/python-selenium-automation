# 3. Create a test case using BDD to verify that a logged-out user can navigate to Sign In:
# Open target.com (given)
# Click Sign In (when)
# From right side navigation menu, click Sign In (when)
# Verify Sign In form opened (then)

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("click Sign In")
def sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()


@then("Verify Sign In form opened")
def verify_sign_in(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'
