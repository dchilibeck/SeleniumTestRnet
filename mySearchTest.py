from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import unittest


class mySearchTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        myUrl = 'http://www.google.ca'

        cls.driver = webdriver.Safari()
        cls.driver.maximize_window()
        cls.driver.get(myUrl)

    def test_search_by_cbc(self):
        searchField = self.driver.find_element_by_id('lst-ib')
        searchField.clear()
        searchField.send_keys('cbc')
        searchField.submit()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='r']/a")))

        self.assertEquals(element.text, 'CBC.ca - Canadian News Sports Entertainment Kids Docs Radio TV')

    def test_search_by_cnn(self):
        searchField = self.driver.find_element_by_id('lst-ib')
        searchField.clear()
        searchField.send_keys('cnn')
        searchField.submit()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='r']/a")))

        self.assertEquals(element.text, 'CNN - Breaking News, Latest News and Videos')

    def test_search_by_mma_fighting(self):
        searchField = self.driver.find_element_by_id('lst-ib')
        searchField.clear()
        searchField.send_keys('mma fighting')
        searchField.submit()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='r']/a")))

        self.assertEquals(element.text, 'MMA Fighting: UFC, Mixed Martial Arts (MMA) News, Results')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
