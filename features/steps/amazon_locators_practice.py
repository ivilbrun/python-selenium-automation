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

