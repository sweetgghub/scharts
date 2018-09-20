# from selenium import webdriver
# from time import sleep
#
# url = "http://stockcharts.com/"
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.get(url)
# sleep(3)
#
# driver.execute_script("window.scrollBy(0,550)")

# JavascriptExecutor jse = (JavascriptExecutor)driver;
# jse.executeScript("window.scrollBy(0,250)", "");
import os, time
folder = time.strftime("%m%d_%Y")
filePath = r"C:\\Users\\George\\Desktop\\stockcharts\\c"
newFilePath = r"C:\\Users\\George\\Desktop\\stockcharts\\" + folder
if os.path.exists(filePath):

    os.rename(filePath, newFilePath)
#
# print(time.strftime("%m%d_%Y"))import time
from datetime import datetime
