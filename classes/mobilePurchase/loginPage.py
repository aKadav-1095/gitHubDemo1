from selenium.webdriver.common.by import By

from Final_seleniumAutomationWithPytest.classes.mobilePurchase.shopPage import ShopPage
from Final_seleniumAutomationWithPytest.utils.browserUtils import BrowserUtils


class LoginPage(BrowserUtils): # creating class for login page

    def __init__(self, driver): # important to pass driver here because we have to use it in methods
        super().__init__(driver)  # we are integrating driver with "super()."
        self.driver = driver # assigning driver to self.driver to use it in other methods
        self.username_input = (By.CSS_SELECTOR, "#username") # tuple format to use in find_element method
        self.password_input = (By.CSS_SELECTOR, "#password")
        self.signInButton = (By.CSS_SELECTOR, "#signInBtn")

    def login_data(self, userName, userPassword):
        self.driver.find_element(*self.username_input).send_keys(userName) # unpacking tuple with * operator
        self.driver.find_element(*self.password_input).send_keys(userPassword)
        self.driver.find_element(*self.signInButton).click()
        shopPage = ShopPage(self.driver) # to eliminate driver param of ShopPage clas, returning shop page object after login action
        return shopPage # returning shop page object to use it in test case

    # def get_title(self):  # this is call for title and common for all classes
    #     return self.driver.title