import math
from selenium import webdriver
import time


link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    browser.switch_to.window(browser.window_handles[1])
    el_value = browser.find_element_by_css_selector("[id=\"input_value\"]").text
    res = calc(el_value)
    browser.find_element_by_css_selector("#answer").send_keys(res)
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
finally:
    time.sleep(5)
    browser.quit()
