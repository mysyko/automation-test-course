from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element_by_css_selector("div.form-group span#input_value")
x = int(element.text)
y = calc(x)

input1 = browser.find_element_by_css_selector("div.form-group input#answer")
input1.send_keys(y)

checkbox1 = browser.find_element_by_id("robotCheckbox")
checkbox1.click()

radiobutton1 = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton1)
radiobutton1.click()

button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()
