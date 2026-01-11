from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Final_seleniumAutomationWithPytest.utils.browserUtils import BrowserUtils


class CheckoutPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver) # we are integrating driver with "super()."
        self.driver = driver
        self.success_button = (By.CSS_SELECTOR, ".btn-success")
        self.country = (By.CSS_SELECTOR, "#country")
        self.checkbox = (By.CSS_SELECTOR, ".checkbox-primary")
        self.submit_button = (By.XPATH, "//input[@type = 'submit']")
        self.success_message = (By.CSS_SELECTOR, ".alert-success")


    def checkout_Data(self):
        self.driver.find_element(*self.success_button).click()


    def purchase_data(self, country):
        self.driver.find_element(*self.country).send_keys(country)
        country_locator = By.LINK_TEXT, "India"
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((country_locator)))
        self.driver.find_element(*country_locator).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def verification_message(self):
        success_message = self.driver.find_element(*self.success_message).text
        assert "Success!" in success_message

    # def get_title(self):  # this is call for title and common for all classes
    #     return self.driver.title



