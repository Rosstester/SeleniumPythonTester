import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

#Defined variables
Server_url = 'https://github.com'
Valid_login = 'just-for-test-login'
Valid_password = 'tester123'
NOT_valid_password = 'tester1234'
Text_to_assert_after_login = 'Learn Git and GitHub without any code!'
Alert_text_after_wrong_login = 'Incorrect username or password.'
Page_title_to_assert = 'GitHub'

#Defined variables for XPath objects
SIGNIN_MAINSITE_BTN = driver.find_element_by_xpath('//*[@href="/login"]')
SIGNIN_LOGINSITE_BTN = driver.find_element_by_xpath('//*[@value="Sign in"]')
LOGIN_FIELD = driver.find_element_by_xpath('//*[@id="login_field"]')
PASSWORD_FIELD = driver.find_element_by_xpath('//*[@id="password"]')
ASSERT_TEXT_AT_LOGINSITE = driver.find_element_by_xpath('//h1[contains(.,'Sign in to GitHub')]')
ASSERT_TEXT_AFTER_LOGIN = driver.find_element_by_xpath('//*[@class="shelf-title"]')
ALERT_TEXT_WRONG_PASSWORD = driver.find_element_by_xpath('//*[@class='container']')

class GitHubLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_to_GitHub_with_valid_credentials(self):
        driver = self.driver
        driver.get(Server_url)
        self.assertIn(Page_title_to_assert, driver.title)
        driver.maximize_window()
        SIGNIN_MAINSITE_BTN.click()
        LOGIN_FIELD.send_keys(Valid_login)
        PASSWORD_FIELD.send_keys(Valid_password)
        SIGNIN_LOGINSITE_BTN.click()
        WAIT = WebDriverWait(driver, 5)
        self.assertEqual(ASSERT_TEXT_AFTER_LOGIN.text, Text_to_assert_after_login)
        driver.close()

    def test_login_to_GitHub_with_NOT_valid_credentials(self):
        driver = self.driver
        driver.get(Server_url)
        self.assertIn(Page_title_to_assert, driver.title)
        driver.maximize_window()
        SIGNIN_MAINSITE_BTN.click()
        LOGIN_FIELD.send_keys(Valid_login)
        PASSWORD_FIELD.send_keys(NOT_valid_password)
        SIGNIN_LOGINSITE_BTN.click()
        WAIT = WebDriverWait(driver, 2)
        self.assertEqual(ALERT_TEXT_WRONG_PASSWORD.text, Alert_text_after_wrong_login)
        driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
