from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from PageObjects import ConfirmPage
from Utilities.BaseClass import BaseClass
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import confirmPage
from PageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_Logger()
        homePage = HomePage(self.driver)  # contructor for driver object
        checkoutpage = homePage.shopItems()       #execution step
        log.info("These are the smartphone listed")
        #checkOutPage = CheckOutPage(self.driver)
        phoneList = checkoutpage.getPhoneList()

        for phone in phoneList:
            phoneName = phone.find_element(By.XPATH, "div/h4/a").text
            log.info(phoneName)
            if phoneName == "Blackberry":
                checkoutpage.getsmartPhone().click()
        log.info("Blackberry selected")

        checkoutpage.getCheckout().click()
        #checkOutPage.getSelectedMbl().click()
        checkoutpage.getTotal()
        ConfirmPage = checkoutpage.getCheckOutButton()
        log.info("you have successfully checkout")
        confirm = confirmPage(self.driver)
        #either we can give send keys values here or in page obj class we can put.
        confirm.getPlace().send_keys("Ind")
        self.waitingTime("India")
        log.info("your Nationality selected")
        confirm.getCountry().click()
        confirm.getCheckbox().click()
        confirm.getButton().click()
        Message = confirm.getMsgTxt().text
        print(Message)
        assert "Success!" in Message

        log.info("product has been ordered successfully!!!!")















