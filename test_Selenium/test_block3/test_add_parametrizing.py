from selenium import webdriver
from selenium.webdriver.common.by import  By
import time
import math
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_correct_answer_in_the_field(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    time.sleep(3)
    input1 = browser.find_element(By.CSS_SELECTOR, 'div .textarea.string-quiz__textarea.ember-text-area.ember-view')
    input1.send_keys(str(answer))
    button = browser.find_element_by_css_selector('button.submit-submission')
    button.click()
    time.sleep(3)
    result = browser.find_element(By.CSS_SELECTOR, 'div .smart-hints__hint')
    expected_result = result.text
    assert expected_result == "Correct!", f"expected result is not the same as received"

