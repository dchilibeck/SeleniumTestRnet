from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import unittest


class ResearchnetTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        myUrl = 'https://staging.researchnet-recherchenet.ca'

        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(myUrl)

    def test_for_splash_page_response(self):
        expected_splash_page_url = "https://staging.researchnet-recherchenet.ca/rnr16/LoginServlet"
        splash_page_url = self.driver.current_url
        print(splash_page_url)
        self.assertEquals(expected_splash_page_url, splash_page_url)

    def test_for_jessionid_cookie(self):
        jsessionid_cookie = self.driver.get_cookie('JSESSIONID')
        self.assertTrue(jsessionid_cookie['value'])

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)