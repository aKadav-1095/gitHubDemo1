from selenium.webdriver.common.by import By

from Final_seleniumAutomationWithPytest.classes.mobilePurchase.checkoutPage import CheckoutPage
from Final_seleniumAutomationWithPytest.utils.browserUtils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)  # we are integrating driver with "super()."
        self.driver = driver
        self.shop_button = (By.XPATH, "//a[contains(@href,'shop')]")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkout = (By.CSS_SELECTOR, ".btn-primary")

    def shop_data(self, mobileName): # here we have make mobile name as parameter

        self.driver.find_element(*self.shop_button).click()
        # Selecting desired mobile with moving position
        product_description = self.driver.find_elements(*self.products)
        # from above list we have to capture list of mobile names
        for list_of_mobiles in product_description:
            mobile = list_of_mobiles.find_element(By.XPATH, "div/h4/a").text  # we will not convert this
            if mobile == mobileName:  # given parameter
                list_of_mobiles.find_element(By.XPATH,"div/button").click()  # this is indirectly linked with product description through list of mobiles.

    def goto_kart_data(self):
        self.driver.find_element(*self.checkout).click()
        checkout = CheckoutPage(self.driver)
        return checkout

    # def get_title(self): # this is call for title and common for all classes
    #     return self.driver.title