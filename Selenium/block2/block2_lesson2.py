from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element_by_css_selector("h2 span#num1")
x = int(element1.text)
element2 = browser.find_element_by_css_selector("h2 span#num2")
y = int(element2.text)
z = x+y
i = str(z)

list_element = Select(browser.find_element_by_css_selector("select#dropdown"))
list_element.select_by_value(i)

button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()

time.sleep(30)
browser.quit()
