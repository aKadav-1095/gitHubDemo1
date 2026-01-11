# Parent Class is for common code across all classes
class BrowserUtils:

    def __init__(self,driver):
        self.driver = driver

    def get_title(self):
       return self.driver.title


# def wait_for_element(driver, locator, timeout=10):
#     return WebDriverWait(driver, timeout).until(
#         EC.presence_of_element_located(locator)
#     )
#
# def take_screenshot(driver, name="screenshot.png"):
#     driver.save_screenshot(name)
