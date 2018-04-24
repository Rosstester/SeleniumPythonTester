import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class GitHubLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_to_GitHub_with_valid_credentials(self):
        driver = self.driver
        driver.get('https://github.com/')
        self.assertIn('GitHub', driver.title)
        driver.maximize_window()
        SIGNIN_MAINSITE_BTN = driver.find_element_by_xpath('//*[@href="/login"]')
        SIGNIN_MAINSITE_BTN.click()
        LOGIN_FIELD = driver.find_element_by_xpath('//*[@id="login_field"]')
        LOGIN_FIELD.send_keys("just-for-test-login")
        PASSWORD_FIELD = driver.find_element_by_xpath('//*[@id="password"]')
        PASSWORD_FIELD.send_keys("tester123")
        SIGNIN_LOGINSITE_BTN = driver.find_element_by_xpath('//*[@value="Sign in"]')
        SIGNIN_LOGINSITE_BTN.click()
        WAIT = WebDriverWait(driver, 5)
        ASSERT_TEXT_AFTER_LOGIN = driver.find_element_by_xpath('//*[@class="shelf-title"]')
        self.assertEqual(ASSERT_TEXT_AFTER_LOGIN.text, 'Learn Git and GitHub without any code!')
        driver.close()

    def test_login_to_GitHub_with_NOT_valid_credentials(self):
        driver = self.driver
        driver.get('https://github.com/')
        self.assertIn('GitHub', driver.title)
        driver.maximize_window()
        SIGNIN_MAINSITE_BTN = driver.find_element_by_xpath('//*[@href="/login"]')
        SIGNIN_MAINSITE_BTN.click()
        LOGIN_FIELD = driver.find_element_by_xpath('//*[@id="login_field"]')
        LOGIN_FIELD.send_keys("just-for-test-login")
        PASSWORD_FIELD = driver.find_element_by_xpath('//*[@id="password"]')
        PASSWORD_FIELD.send_keys("tester1234")
        SIGNIN_LOGINSITE_BTN = driver.find_element_by_xpath('//*[@value="Sign in"]')
        SIGNIN_LOGINSITE_BTN.click()
        WAIT = WebDriverWait(driver, 2)
        ALERT_TEXT_WRONG_PASSWORD = driver.find_element_by_xpath("//*[@class='container']")
        self.assertEqual(ALERT_TEXT_WRONG_PASSWORD.text, 'Incorrect username or password.')
        driver.close()

#SIGNIN_MAINSITE_BTN = driver.find_element_by_xpath('//*[@href="/login"]')
#SIGNIN_LOGINSITE_BTN = driver.find_element_by_xpath('//*[@value="Sign in"]')
#LOGIN_FIELD = driver.find_element_by_xpath('//*[@id="login_field"]')
#PASSWORD_FIELD = driver.find_element_by_xpath('//*[@id="password"]')
#ASSERT_TEXT_AT_LOGINSITE = driver.find_element_by_xpath('//h1[contains(.,'Sign in to GitHub')]')
#ASSERT_TEXT_AFTER_LOGIN = driver.find_element_by_xpath('//*[@class="shelf-title"]')
#ALERT_TEXT_WRONG_PASSWORD = driver.find_element_by_xpath('//*[@class='container']')



if __name__ == '__main__':
    unittest.main()
