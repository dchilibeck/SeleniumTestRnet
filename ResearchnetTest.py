from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import unittest
import time


class ResearchnetTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print('setup called')
        myUrl = 'https://staging.researchnet-recherchenet.ca'

        #cls.driver = webdriver.Firefox()
        cls.driver = webdriver.Chrome('/Users/dchilibeck/Downloads/chromedriver')
        cls.driver.maximize_window()
        cls.driver.get(myUrl)

    def test_for_splash_page_response(self):
        print('test_for_splash_page_response called')
        expected_splash_page_url = "https://staging.researchnet-recherchenet.ca/rnr16/LoginServlet"
        splash_page_url = self.driver.current_url

        self.assertEquals(expected_splash_page_url, splash_page_url)

    def test_for_jessionid_cookie(self):
        print('test_for_jessionid_cookie called')
        jsessionid_cookie = self.driver.get_cookie('JSESSIONID')
        self.assertTrue(jsessionid_cookie['value'])

    def test_for_successful_login(self):
        print('test_for_successful_login called')

        expected_workspace_url = "https://staging.researchnet-recherchenet.ca/rnr16/myActivities.do"

        self.driver.find_element_by_link_text('English').click()
        username = self.driver.find_element_by_id('j_username')
        password = self.driver.find_element_by_id('j_password')
        username.send_keys('dchilibeck1210@gmail.com')
        password.send_keys('1.4M.4rch1t3ct!')
        self.driver.find_element_by_class_name('rn-btn-green').submit()
        current_url = self.driver.current_url
        self.driver.get('https://staging.researchnet-recherchenet.ca/rnr16/j_spring_security_logout')

        self.assertEquals(expected_workspace_url, current_url)

    @classmethod
    def tearDown(cls):
        print('tearDown called')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)