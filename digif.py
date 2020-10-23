from selenium import webdriver
import os
import random
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://digifabster.com/4taps/client/upload/")

upload_button = driver.find_element_by_name("qqfile")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'sample.stl') 
upload_button.send_keys(file_path)

next_button = driver.find_element_by_xpath('//*[@id="next_step_btn"][not(contains(@class, "disabled"))]')
next_button.click()

rand = random.randint(1, 999999999999)
email_field = driver.find_element_by_id("id_get_user_email_form-email")
email_field.send_keys(f"test+{rand}@email.com")
set_email_button = driver.find_element_by_xpath('//*[@id="set_email"][not(contains(@class, "disabled"))]')
add_to_cart_button = driver.find_element_by_xpath('//*[@class="btn add_to_cart_btn"][not(contains(@class, "disabled"))]')
set_email_button.click()

driver.find_element_by_id("id_first_name").send_keys("John")
driver.find_element_by_id("id_last_name").send_keys("Smith")
driver.find_element_by_id("id_phone_number").send_keys("123456789")
driver.find_element_by_id("extra_info_btn").click()

driver.find_element_by_id("continue_to_widget").click()
add_to_cart_button.click()
driver.find_element_by_xpath('//*[@class="btn btn-next"][not(contains(@class, "disabled"))]').click()

driver.find_element_by_css_selector(".increase-startup-price-link").click()
driver.find_element_by_css_selector(".btn.btn-next.pull-right").click()

time.sleep(5)
driver.quit()
