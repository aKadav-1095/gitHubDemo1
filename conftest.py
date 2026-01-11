import os

import time

import pytest
from selenium import webdriver
driver = None


# We can get this from internet if we search method to register options
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome", help = "browser selection"
    )
# here - "<--option to register>, action = "store_true", default = "<browser name which could be default in case of not mention>"
        # help = <description of option use>

# @pytest.fixture() # this for single browser
# def browserInstance():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver # R - driver instance will be returned to test case
#     driver.quit() # closing the browser after test case execution



# to make browser selection dynamic - IMP
@pytest.fixture()
def browserInstance(request):
    global driver# we have to give instance here as request
    browser_name = request.config.getoption("browser_name") # we have to request get option from here as "browse_name" and assign it to variable as "browser_name"
    # driver = None # NI - used because we have to use it in if-else condition, so to avoid error we have to initialize it with None
    # Imp - we have to register our options as here "browser_name" is option before using it
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else: # If browser name is wrong for trying with any other browser
        raise pytest.UsageError(f"Unsupported browser: {browser_name}")
    driver.implicitly_wait(10) # it will apply for all browsers
    driver.maximize_window() # it will apply for all browsers

    yield driver # R - driver instance will be returned to test case
    driver.quit() # closing the browser after test case execution can use driver.close()


# def _capture_screenshot(file_name): # created from hook wrapper to crate capture screenshot in selenium
#     driver.get_screenshot_as_file(file_name)


# python
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # try to get webdriver instance from fixture 'browserInstance'
            driver_instance = item.funcargs.get("browserInstance", None)
            # fallback to module-level global if used
            driver_instance = driver_instance or globals().get("driver", None)

            if driver_instance and pytest_html:
                reports_dir = os.path.join(os.getcwd(), "reports")
                os.makedirs(reports_dir, exist_ok=True)
                file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
                try:
                    driver_instance.get_screenshot_as_file(file_name)
                    html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    )
                    extra.append(pytest_html.extras.html(html))
                except Exception:
                    # ignore screenshot errors to not break reporting
                    pass
        report.extra = extra



