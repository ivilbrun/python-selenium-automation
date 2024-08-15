from selenium import webdriver  #
from selenium.webdriver.common.by import By  # imports (by.id, xpath, ect___)
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep  # used to tell the code to wait in before continuing

# get the path to the ChromeDriver executable, connects to google chrome and starts it
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # makes the browser full screen


# 1. amazon locators practice
# # amazon logo
# driver.find_element(By.XPATH, "//div[@id='a-page']//i[contains(@class, 'a-icon a-icon-logo')]")
#
# # email field
# driver.find_element(By.ID, 'ap_email')
#
# # continue button
# driver.find_element(By.ID, 'continue')
#
# # conditions of use link
# driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'condition_of_use')]")
#
# # privacy notice
# driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[contains(@href, 'privacy notice')]")
#
# # need help link ? not sure about this one
# driver.find_element(By.XPATH, "//span[contains(@class, 'a-expander-prompt')]")
#
# # forgot your password link
# driver.find_element(By.ID, 'auth-fpp-link-bottom')
#
# # other issues with sign in link
# driver.find_element(By.ID, 'ap-other-signin-issues-link')
#
# # create your amazon account button
# driver.find_element(By.ID, 'createAccountSubmit')

# 2. Test Case: Users can navigate to SignIn page

driver.get('https://www.target.com/')
sleep(3)

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(3)

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(3)

assert 'create_session_signin' in driver.current_url.lower(), f"Expected behavior did not return"
print('Test passed')

driver.quit()
