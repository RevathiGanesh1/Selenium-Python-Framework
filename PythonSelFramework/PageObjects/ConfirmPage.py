from selenium.webdriver.common.by import By


class confirmPage:

    def __init__(self, driver):
        self.driver = driver


    #1 self.driver.find_element(By.ID, "country").send_keys("Ind")
    place = (By.ID,"country")
    #2 self.driver.find_element(By.LINK_TEXT, "India").click()
    country = (By.LINK_TEXT, "India")
    #3 self.driver.find_element(By.CLASS_NAME, "checkbox").click()
    checkBox = (By.CLASS_NAME, "checkbox")
    #4 self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
    Button = (By.CSS_SELECTOR, "input[value='Purchase']")
    #5 Message = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-dismissible']").text
    MsgText = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def getPlace(self):
        return self.driver.find_element(*confirmPage.place)     #either we can giv e send keys values here or in test class we can put.

    def getCountry(self):
        return self.driver.find_element(*confirmPage.country)

    def getCheckbox(self):
        return self.driver.find_element(*confirmPage.checkBox)

    def getButton(self):
        return self.driver.find_element(*confirmPage.Button)

    def getMsgTxt(self):
        return self.driver.find_element(*confirmPage.MsgText)

