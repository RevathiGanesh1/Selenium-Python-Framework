
import pytest
#from pip._internal.utils import datetime

#import datetime
#datetime.datetime.now()
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/Users/HP/PycharmProjects/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:/Users/HP/PycharmProjects/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        print("Microsoft edgee, eeeeeeeeeeeeeee")

    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


#screenshot report file
#@pytest.hookimpl(hookwrapper=True)
#def pytest_runtest_makereport(item, call):
#    now = datetime.now()
#    pytest_html = item.config.pluginmanager.getplugin('html')
#    outcome = yield
#    report = outcome.get_result()
#    extra = getattr(report, 'extra', [])
#    if report.when == 'call' or report.when == "setup":
#        xfail = hasattr(report, 'wasxfail')
#        if (report.skipped and xfail) or (report.failed and not xfail):
#            file_name = report.nodeid.replace("::", "_") + ".png"
#            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
#            # _capture_screenshot(file_name)
#            if file_name:
#                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                extra.append(pytest_html.extras.html(html))
#        report.extra = extra


#def _capture_screenshot(name, driver):
#    driver.get_screenshot_as_file(name)


#def pytest_html_report_title(report):
#    report.title = "Rev Automation Report"

