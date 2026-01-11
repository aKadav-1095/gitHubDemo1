from selenium.webdriver.common.by import By


class SortingTable:

    def __init__(self,driver):
        self.driver = driver
        self.sort = (By.XPATH, "//span[text()='Veg/fruit name']")
        self.sorted_list = (By.XPATH, "//td[1]")



    def sortingTable_data(self):
        # click on sorting of table of web page
        self.driver.find_element(*self.sort).click()
        # Collecting the sorted items in list
        webSortedItems = []
        web_items = self.driver.find_elements(*self.sorted_list)
        for eachItem in web_items:
            webSortedItems.append(eachItem.text)
            # print(webSortedItems)
        # assertion, with original list
        original_sorted_items = sorted(webSortedItems)
        # print(original_sorted_items)
        assert original_sorted_items == webSortedItems

