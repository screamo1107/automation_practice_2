from selenium import webdriver
import math
import time


def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el_value = browser.find_element_by_css_selector("[id='treasure']")
    res = calc(el_value.get_attribute('valuex'))

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
