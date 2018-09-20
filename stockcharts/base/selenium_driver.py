from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import stockcharts.utilities.custom_logger as cl
import logging

class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            # print("Locator type " + locatorType + " not correct/supported")
            self.log.info(f"Locator type, {locatorType} is not correct/supported")
        return False



    def getElement(self, locatorType, locator):
        locatorType = locatorType.lower()
        try:
            element = self.driver.find_element(self.getByType(locatorType), locator)
            # print("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
            self.log.info(f"Element found with locator: {locator} and locatorType: {locatorType}.")
            return element
        except:
            self.log.info(f"Element not found with locator: {locator} and locateoType: {locatorType}")
            return None


    def elementClick(self, locatorType, locator):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorType, locator)
            element.click()
            self.log.info(f"Clicked on element with locator: {locator} an locatorTpe: {locatorType}.")
            return None
        except:
            self.log.info(f"Cannot click on the element with locator: {locator} and locatorType: {locatorType}.")
            print_stack()

    def sendKey(self, locatorType, locator, data):
        try:
            element = self.getElement(locatorType, locator)
            element.send_keys(data)
            self.log.info(f"Sent data on element with locator: {locator} and locatorType: {locatorType}.")
        except:
            self.log.info(f"Cannot send data on the element with locator: {locator} and locatorType: {locatorType}.")
            print_stack()


    def isElementExist(self, locatorType, locator):
        locatorType = locatorType.lower()
        try:
            element = self.getElement(locatorType, locator)
            self.log.info(f"Element Found")
            return True

        except:
            self.log.info(f"Element not found")
            return False

    def getDropDownOption(self, locatorType, locator, selectOption, data):
        locatorType = locatorType.lower()
        try:
            element = self.getElement(locatorType, locator)
            self.log.info(f"Dropdown select element Found: {element}.")
            sel = Select(element)
            selectOption = selectOption.lower()
            if selectOption == "value":
                sel.select_by_value(data)
            elif selectOption == "index":
                sel.select_by_index(data)
            elif selectOption == "text":
                sel.select_by_visible_text(data)
                #To be deleted following print statement
                self.log.info(f"Select by {data}")
            else:
                self.log.info(f"no such option: {data}.")
        except:
            self.log.info(f"Select element not exist: {locator}.")
        return None


    def slider(self, locatorType, locator, data):
        element = self.getElement(locatorType, locator)
        try:
            actions = ActionChains(drvier)
            actions.drag_and_drop_by_offset(element, 0, 200).perform()
            self.log.info(f"Sliding element successful.")
        except:
            self.log.info(f"Sliding failed on element")



    def waitForElement(self):
        pass