from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1").text
    num2 = browser.find_element_by_css_selector("#num2").text
    res = int(num1) + int(num2)

    browser.find_element_by_css_selector("#dropdown").click()
    browser.find_element_by_css_selector(("[value = \"{}\"]".format(res))).click()
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
finally:
    time.sleep(5)
    browser.quit()
