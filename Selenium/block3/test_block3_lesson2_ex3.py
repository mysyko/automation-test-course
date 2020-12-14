from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual("Congratulations! You have successfully registered!", final_text, "Text do not match")
        #assert "Congratulations! You have successfully registered!" == final_text
        time.sleep(2)
        browser.quit()

    def test_abs2(self):
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
        self.assertEqual("Congratulations! You have successfully registered!", final_text, "Text do not match")
        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
