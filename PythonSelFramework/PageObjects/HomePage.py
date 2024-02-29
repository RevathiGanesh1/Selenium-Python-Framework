from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):                                   #This is defining method.so we can use this method in test class
        self.driver.find_element(*HomePage.shop).click()   #This is to defining the shop locator here isntead of showing in execution class
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

#here we are using instance variable and class variable!!!!
#here we have used constructor o.e. __init__  -> which is used to inialize/creating object instance at that class.
# we have used inheritance this class with test e2e.

# ******************Test class 2*******************

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")

    subButton = (By.XPATH, "//input[@type='submit']")
    alertTxt = (By.CLASS_NAME, "alert-success")
    EmpStatus = (By.CSS_SELECTOR, "#inlineRadio2")
    msg = (By.XPATH, "(//input[@type='text'])[3]")


    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getButton(self):
        return self.driver.find_element(*HomePage.subButton)

    def getAlertText(self):
        return self.driver.find_element(*HomePage.alertTxt)

    def getEmpStatus(self):
        return self.driver.find_element(*HomePage.EmpStatus)

    def getMessage(self):
        return self.driver.find_element(*HomePage.msg)

