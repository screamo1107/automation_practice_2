from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        elem1 = browser.find_element_by_css_selector(".first:required")
        elem1.send_keys('q')
        elem2 = browser.find_element_by_css_selector(".second:required")
        elem2.send_keys('q')
        elem3 = browser.find_element_by_css_selector(".third:required")
        elem3.send_keys('q')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(3)

        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Text is wrong or not presented")
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        elem1 = browser.find_element_by_css_selector(".first:required")
        elem1.send_keys('q')
        elem2 = browser.find_element_by_css_selector(".second:required")
        elem2.send_keys('q')
        elem3 = browser.find_element_by_css_selector(".third:required")
        elem3.send_keys('q')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(3)

        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Text is wrong or not presented")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
