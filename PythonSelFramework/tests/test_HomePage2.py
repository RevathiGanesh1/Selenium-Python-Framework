import logging

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from PageObjects.HomePage import HomePage
from TestData import TestDataHP2
from TestData.TestDataHP2 import test_testData
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestHomePage2(BaseClass):

    def test_formSubmission(self, getData):
        log = self.get_Logger()
        homepage = HomePage(self.driver)
        #homepage.getName().send_keys(getData[0])
        homepage.getName().send_keys(getData["firstname"])
        log.info("Your firstname is entered")
        homepage.getEmail().send_keys("revathinetlink@gmail.com")
        log.info("Your email ID is entered")
        homepage.getPassword().send_keys("12345")
        log.info("Your password is entered")
        homepage.getCheckbox().click()
        log.info("checkbox is selected")

        # static dropdown
        #self.selectOptionbyText(homepage.getDropdown(), 0, getData[2])
        self.selectOptionbyText(homepage.getDropdown(), 0, getData["gender"])
        homepage.getButton().click()
        message = homepage.getAlertText().text
        print(message)
        log.info("Alert message is successfully pop up in display")
        assert "success" in message


        homepage.getEmpStatus().click()
        homepage.getMessage().send_keys("Heyy Reyy!!")
        log.info("Text Box filled up with Heyyy Reyyyy!!!!!!!!!")
        # driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
        self.driver.refresh()

       # assert "dsmnjsvjsbv" in homepage.getMessage()

#params supports both dictionary and tuple data types
    #@pytest.fixture(params=[{"firstname" :"Revathi", "gender": "Female"},{"firstname": "Ranjith","gender": "Male"}])
    @pytest.fixture(params= test_testData.test_fieldValues )
    def getData(self, request):
        return request.param
