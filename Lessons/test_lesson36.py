import math
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Required for number calculation
def check_the_answer():
    return str(math.log(int(time.time())))


class TestSuit1:
    @pytest.mark.parametrize("link", ["236895", "236896", "236897", "236898", "236899",
                                      "236903", "236904", "236905"])
    def test_different_links(self, browser, link):
        browser.get("https://stepik.org/lesson/{}/step/1".format(link))

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea")))
        browser.find_element_by_css_selector(".textarea").send_keys(check_the_answer())

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
        browser.find_element_by_css_selector(".submit-submission").click()

        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        hint = browser.find_element_by_css_selector(".smart-hints__hint").text

        assert hint == "Correct!", "Hint is wrong or not shown!"
