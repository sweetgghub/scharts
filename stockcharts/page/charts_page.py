from stockcharts.base.selenium_driver import SeleniumDriver
import stockcharts.utilities.custom_logger as cl
import logging

class ChartsPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchField = "//input[@id='navsearchtext']"
    _buttonGo = "//button[@id='nav-search-symbol-go-btn']"

    _dropDownElement = "//select[@id='favoritesLoad']"



    def enterSearch(self, symbol):
        self.sendKey("xpath", self._searchField, symbol)
        self.elementClick("xpath", self._buttonGo)

    def getSavedCharts(self, data):
        self.getDropDownOption("xpath", self._dropDownElement, "text", data)
