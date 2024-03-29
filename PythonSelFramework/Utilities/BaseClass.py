import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_Logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s:%(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger

    def waitingTime(self, text):
        eWait = WebDriverWait(self.driver, 10)
        eWait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))


    def selectOptionbyText(self, locator,value, text):
        dropdown = Select(locator)
        dropdown.select_by_index(value)
        dropdown.select_by_visible_text(text)



