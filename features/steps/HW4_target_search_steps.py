from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)
    # context.app.header.search_product()


# @then('Verify search worked')
# def verify_search_results(context):
#     expected_text = 'product_outcome'
#     actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'


@then('Verify search results shown for {product_outcome}')
def verify_search_results(context, product_outcome):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product_outcome in actual_text, f'Expected {product_outcome} not in actual {actual_text}'


@then('Verify correct search results URL opens for {product_outcome}')
def verify_url(context, product_outcome):
    url = context.driver.current_url
    assert product_outcome in url, f'Expected {product_outcome} not in {url}'

