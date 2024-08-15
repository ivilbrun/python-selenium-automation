from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 2. Create a test case using BDD that
# opens target.com, (given)
# clicks on the cart icon (when)
# and verifies that “Your cart is empty” message is shown: (then)


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("Click on Cart icon")
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(2)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


# 3. Create a test case using BDD to verify that a logged-out user can navigate to Sign In:
# Open target.com (given)
# Click Sign In (when)
# From right side navigation menu, click Sign In (when)
# Verify Sign In form opened (then)

@when("click Sign In")
def sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()


@then("Verify Sign In form opened")
def verify_sign_in(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'


# # OR: driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
# or
# # Make sure login button is shown
# driver.find_element(By.ID, 'login')


# 1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements:
#
# # logo
# driver.find_element(By.XPATH, "//div[@id='a-page']//i[contains(@class, 'a-icon a-icon-logo')]")
#
# # create account
# driver.find_element(By.XPATH, "//form[@id='ap_register_form']//h1[contains(@class, 'a-spacing-small')]")
#
# # name field
# driver.find_element(By.ID, 'ap_customer_name')
#
# # mobile number or email field
# driver.find_element(By.ID, 'ap_email')
#
# # password field
# driver.find_element(By.ID, 'ap_password')
#
# # re-enter password field
# driver.find_element(By.ID, 'ap_password-check')
#
# # continue field
# driver.find_element(By.ID, 'continue')
#
# # conditions of use link
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'condition_of_use')]")
#
# # privacy notice link
# driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[contains(@href, 'privacy notice')]")
#
# # sign in link
# driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")
