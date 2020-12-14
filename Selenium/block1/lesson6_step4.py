from selenium import webdriver
import time

try:
    #Вставлена ссылка для проверки получения ошибки NoSuchElementException
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
    input1.send_keys("Test")
    input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
    input2.send_keys("Test2")
    input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
    input3.send_keys("test@test.com")

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

    time.sleep(2)

    find_final_text = browser.find_element_by_tag_name("h1")
    final_text = find_final_text.text
    assert "Congratulations! You have successfully registered!" == final_text

finally:

    time.sleep(2)
    browser.quit()
