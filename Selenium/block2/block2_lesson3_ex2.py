from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button1.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

element = browser.find_element_by_id("input_value")
x = int(element.text)
y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y)

button2 = browser.find_element_by_css_selector("button.btn.btn-primary")
button2.click()

time.sleep(30)
browser.quit()