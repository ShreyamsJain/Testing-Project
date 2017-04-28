import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("https://www.groupon.com")
# get the search textbox
#sign_in = 
driver.find_element_by_id("nothx").click()
time.sleep(5)
window_before = driver.window_handles[0]
driver.find_element_by_id("ls-user-signin").click()
#driver.find_element_by_link_text("Sign In").send_keys("\n")
time.sleep(5)
#window_after = driver.window_handles[1]
#driver.switch_to_window(window_after)
email_input = driver.find_element_by_id("email-input")
pwd_input = driver.find_element_by_id("password-input")
# enter search keyword and submit
email_input.send_keys("shreyams.jain@sjsu.edu")
pwd_input.send_keys("1Groupon1$")
pwd_input.submit()

time.sleep(3)
element_to_hover_over = driver.find_element_by_css_selector(".icon-arrow-down-large")

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

time.sleep(1)

driver.find_element_by_id("user-giftcard").click()
time.sleep(3)
driver.find_element_by_id("send_plastic_card").click()
time.sleep(3)

window_2 = driver.window_handles[1]
driver.switch_to_window(window_2)

driver.find_element_by_css_selector(".head").click()
time.sleep(3)

window_3 = driver.window_handles[2]
driver.switch_to_window(window_3)


element_to_hover_over = driver.find_element_by_css_selector(".icon-arrow-down-large")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

time.sleep(1)
driver.find_element_by_id("sign-out").click()

time.sleep(3)
driver.quit()
