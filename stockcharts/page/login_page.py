from stockcharts.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _loginLink = "//li[@id='navbar-login']//a[@href='/login']"

    _userIDField = "//input[@id='form_UserID']"
    _passwordField = "//form[@id='loginform']//input[@name='form_UserPassword']"
    _findCourseField = "//input[@id='search-courses']"
    _logInButton = "//form[@id='loginform']//button[@type='submit']"

    #click loginLink
    def clickLoginLink(self):
        self.elementClick("xpath", self._loginLink)


    #enter email
    def enterUserID(self, userid):
        self.sendKey("xpath", self._userIDField, userid)


    #enter password
    def enterPassword(self, password):
        self.sendKey("xpath", self._passwordField  , password)

    #click loginButton
    def clickLoginButton(self):
        self.elementClick("xpath", self._logInButton)

    #login
    def login(self, userid, password):
        self.clickLoginLink()
        self.enterUserID(userid)
        self.enterPassword(password)
        self.clickLoginButton()