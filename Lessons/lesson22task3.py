import os
from selenium import webdriver
import time


file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'some_file.txt')
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name=\"firstname\"]").send_keys("q")
    browser.find_element_by_css_selector("[name=\"lastname\"]").send_keys("q")
    browser.find_element_by_css_selector("[name=\"email\"]").send_keys("q")
    browser.find_element_by_css_selector("[type=\"file\"]").send_keys(file_path)
    browser.find_element_by_css_selector("[type = 'submit']").click()
finally:
    time.sleep(5)
    browser.quit()
