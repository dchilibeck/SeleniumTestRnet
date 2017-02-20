from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

ff = webdriver.Firefox()
ff.get("http://www.google.ca")

try:
    searchField = ff.find_element_by_id('lst-ib')
    searchField.clear()
    searchField.send_keys('cbc')
    searchField.submit()

    element = WebDriverWait(searchField, 25).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='r']/a")))

    print(element.text)

    if element:
        print('Element Was Found')

finally:
    ff.quit()