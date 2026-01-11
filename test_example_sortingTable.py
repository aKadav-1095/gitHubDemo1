import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Final_seleniumAutomationWithPytest.classes.sortingTable.sortingTable import SortingTable

@pytest.mark.smoke
def test_sortingTable(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    sortingTable = SortingTable(driver)
    sortingTable.sortingTable_data()
