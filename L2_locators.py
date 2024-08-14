from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# types of locators
# By ID — ids of the elements should be unique for the page;
# this is the most efficient and fast way to locate an element
#
# By XPATH — locates an element using DOM structure of
# the page. This is the type of locator that is always available
# for an element, even more, there are usually various
# possible XPATHs
#
# By CSS Selector — CSS selectors are another alternative
# of finding elements. This is useful for locating items that
# have a unique style on the page
#
# By Class — class name locator finds the element which
# matches the value specified in the attribute name class
#
# By Name — if there is no id to use in HTML code, another
# preferred way to locate the web element is ‘name’ attribute
#
# By TagName — this kind of locator is used to find the element
# matching the specified Tag Name
#
# By LinkText — if there are any link on the page, it’s very easy
# to locate them, but make sure, there is one unique link on that
# web page.
#
# By Partial LinkText — this locator works the same way as the
# LinkText one, but it gives user the opportunity to handle more
# dynamic links from the pages, as the element can be find by
# a partial link text

# the attributes; id and class are referred to as the element selector

# find by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-logo-sprites')

# find by XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

# tag > attribute(s) > value
# $x("//tag[@attribute='value']")
# driver.find_element(By.XPATH, "//tag[@attribute='value']")

# tag -
# the word after <, <label, <input, <div
# attribute -
# value -

# find by attribute only
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")
# find by multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @type='text' and @dir='auto']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @type='text']")

driver.find_element(By.ID, 'searchDropdownBox')  # driver.find_element(By.XPATH, "//select[@ID='searchDropdownBox']")

# by text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# text() and attributes
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and text()='Best Sellers']")
# connecting to parent node
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
# contains()
driver.find_element(By.XPATH, "//h2[contains(text(), 'under $30')]")
