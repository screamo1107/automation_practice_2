from selenium import webdriver
import time
import math


def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el_value = browser.find_element_by_css_selector("[id='input_value']").text
    res = calc(el_value)

    browser.execute_script("window.scrollBy(0, 100);")

    elem1 = browser.find_element_by_css_selector("#answer")
    elem1.send_keys(res)

    elem2 = browser.find_element_by_css_selector("[id=\"robotCheckbox\"]")
    elem2.click()

    elem3 = browser.find_element_by_css_selector("[id=\"robotsRule\"]")
    elem3.click()

    elem4 = browser.find_element_by_css_selector("[type = 'submit']")
    elem4.click()

    time.sleep(1)
finally:
    time.sleep(3)
    browser.quit()
