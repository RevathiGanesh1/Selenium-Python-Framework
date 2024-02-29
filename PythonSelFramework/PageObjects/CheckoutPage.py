from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import confirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    #1 driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    phones = (By.XPATH,"//div[@class='card h-100']")
    #2 phone.find_element(By.XPATH, "div/button").click()
    smartPhone = (By.XPATH,"//button[@class='btn btn-info']")

    chckOut = (By.XPATH,"//li/a[@class='nav-link btn btn-primary']")
    #3 self.driver.find_element(By.XPATH, "//div/ul/li/a").click()
    #selected = (By.XPATH,"//div/ul/li/a")
    #selected = (By.ID,"checkbox2")
    #4 self.driver.find_element(By.CSS_SELECTOR, "td h3 strong").text
    total = (By.CSS_SELECTOR,"td h3 strong")
    #5 self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn btn-success']").click()
    checkOutButton = (By.CSS_SELECTOR,"button[class*='btn btn-success']")

    def getPhoneList(self):
        return self.driver.find_elements(*CheckOutPage.phones)

    def getsmartPhone(self):
        return self.driver.find_element(*CheckOutPage.smartPhone)

    def getCheckout(self):
        return self.driver.find_element(*CheckOutPage.chckOut)
   # def getSelectedMbl(self):
    #    return self.driver.find_element(*CheckOutPage.selected)

    def getTotal(self):
        return self.driver.find_element(*CheckOutPage.total)

    def getCheckOutButton(self):
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        ConfirmPage = confirmPage(self.driver)
        return ConfirmPage


