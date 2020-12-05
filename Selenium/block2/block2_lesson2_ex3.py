from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("div.form-group input[name='firstname']")
input1.send_keys("test")
input2 = browser.find_element_by_css_selector("div.form-group input[name='lastname']")
input2.send_keys("test")
input3 = browser.find_element_by_css_selector("div.form-group input[name='email']")
input3.send_keys("test")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
dowload_file = browser.find_element_by_id("file")
dowload_file.send_keys(file_path)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()
