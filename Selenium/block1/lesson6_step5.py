from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element_by_css_selector("div.form-group img#treasure")
x = element.get_attribute("valuex")
y = calc(x)

input1 = browser.find_element_by_css_selector("div.form-group input#answer")
input1.send_keys(y)

checkbox1 = browser.find_element_by_css_selector("div.form-group #robotCheckbox")
checkbox1.click()

radiobutton1 = browser.find_element_by_css_selector("div.form-group #robotsRule")
radiobutton1.click()

button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()

time.sleep(30)
browser.quit()