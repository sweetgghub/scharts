from selenium import webdriver
from stockcharts.page.login_page import LoginPage
from selenium.webdriver.common.by import By
import unittest

class LoginTests(unittest.TestCase):

    def testLogin(self):

        url = "http://stockcharts.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url)

        userid = "gguan86@outlook.com"
        password = "moorpark"
        userService = "//div[@id='userService']//span[text()='Basic']"

        lg = LoginPage(driver)
        lg.login(userid, password)

        try:
            ms = lg.isElementExist("xpath", userService)
            if ms:
                print(f"login test passed")
            else:
                print(f"login test failed")
        except:
            print("test failed")

        driver.close()

