from selenium import webdriver
from stockcharts.page.login_page import LoginPage
from stockcharts.page.charts_page import  ChartsPage
from selenium.webdriver.common.by import By
import unittest
import time
from time import sleep
import os, shutil
import stockcharts.utilities.custom_logger as cl
import logging
class LoginTests(unittest.TestCase):


    # log = cl.customLogger(logging.DEBUG)
    def testCharts(self):

        url = "http://stockcharts.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url)

        userid = "gguan86@outlook.com"
        password = "moorpark"
        userService = "//div[@id='userService']//span[text()='Basic']"
        spx1hour = "$ SPX - 1 hour"
        spxDaily = "$ SPX - Daily"
        spxWeekly = "$ SPX weekly"
        spxMonthly = "$ SPX - Monthly 2"
        nasdq1hour = "$ Nasdaq 1hour"
        nasdqDaily = "$ Nasdaq Daily"
        nasdqWeekly = "$ Nasdaq weekly"
        nasdqMonthly = "$ Nasdaq Monthly"
        dow1hour = "$ Dow 1hour"
        dowDaily = "$ Dow Daily"
        dowWeekly = "$ Dow Weekly"
        dowMonthly = "$ Dow Monthly"


        def takeScreenshot(file_destination):
            try:
                driver.save_screenshot(file_destination)
                print(f"screenshot saved to: {file_destination}")
            except NotADirectoryError:
                print(f"no such directory")

        indexs = [[spx1hour, spxDaily, spxWeekly, spxMonthly],
                  [nasdq1hour, nasdqDaily, nasdqWeekly, nasdqMonthly],
                  [dow1hour, dowDaily, dowWeekly, dowMonthly]]

        def saveChartsToFolder(indexs):

            print(f"Run method: saveChartsToFolder()")

            for x in indexs:
                for y in x:

                    charts.getSavedCharts(y)
                    driver.execute_script("window.scrollBy(0,250)")
                    sleep(2)
                    fileDestination =filePath + "\\" + y + ".png"
                    takeScreenshot(fileDestination)




        lg = LoginPage(driver)
        lg.login(userid, password)

        charts = ChartsPage(driver)
        charts.enterSearch("spx")

        folder = time.strftime("%m%d_%Y")
        # filePath = r"C:\\Users\\George\\Desktop\\stockcharts\\" + old
        filePath = r"C:\\Users\\George\\Desktop\\stockcharts\\" + folder
        if not os.path.exists(filePath):
            os.makedirs(filePath)

        else:
            shutil.rmtree(filePath)
            os.makedirs(filePath)

        saveChartsToFolder(indexs)

        # driver.close()


