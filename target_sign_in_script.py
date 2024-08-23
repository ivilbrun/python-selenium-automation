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

# Test Case: Users can navigate to SignIn page

driver.get('https://www.target.com/')
sleep(3)

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(3)

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(3)

assert 'create_session_signin' in driver.current_url.lower(), f"Expected behavior did not return"
print('Test passed')

driver.quit()
