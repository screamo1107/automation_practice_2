import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))
    browser.find_element_by_css_selector("#book").click()

    el_value = browser.find_element_by_css_selector("[id=\"input_value\"]").text
    res = calc(el_value)
    browser.find_element_by_css_selector("#answer").send_keys(res)
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
finally:
    time.sleep(5)
    browser.quit()
