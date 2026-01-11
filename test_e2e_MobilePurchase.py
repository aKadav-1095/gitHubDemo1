import json

import pytest

from Final_seleniumAutomationWithPytest.classes.mobilePurchase import loginPage
from Final_seleniumAutomationWithPytest.classes.mobilePurchase.loginPage import LoginPage

# to read Json file
# 1st take file path in one variable
# open it with "with open (<variableName>) as <anyName>
# take any name and parametrise it with json.load(<anyName> and assign it to variableName
# with created variable retrieve desired data with index and assign it to variable

testDataPath = "..\\Final_seleniumAutomationWithPytest\\data\\test_e2e_MobilePurchase.json"
with open(testDataPath) as file:
    data_file = json.load(file)
    test_data = data_file["data"]  # we have to call data with index

@pytest.mark.parametrize("testItemList",test_data)  # we have to parameterized file with fixture and assign it to variable
def test_mobile_purchase(browserInstance, testItemList):  # we have to give variable name as parameter
    driver = browserInstance  # we have called fixture here assigned it to variable as driver
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage_action = LoginPage(driver)  # creating object of LoginPage class and passing driver to it.
    # loginPage.login_data() # calling method of login page class through object to perform login action.
    print(loginPage_action.get_title()) # we have called util here
    shopPage_action = loginPage_action.login_data(testItemList["userName"], testItemList["userPassword"])  # we eliminated above class as we have added driver to login_data method and assigned it to a variable
    shopPage_action.shop_data(testItemList["productName"])  # calling .shop_data method through shopPage object and given desired MobileName through parameter
    print(shopPage_action.get_title())
    checkout_action = shopPage_action.goto_kart_data()  # calling .goto_kart method through shopPage object, and we have added ShopPage class driver
    checkout_action.checkout_Data()
    checkout_action.purchase_data("ind")  # given desired MobileName through parameter
    checkout_action.verification_message()
