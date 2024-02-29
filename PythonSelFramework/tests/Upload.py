
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

fruit_name = "Apple"
file_path = "C:\\Users\\HP\\Downloads\\download.xlsx"
#service_obj = Service()
#driver = webdriver.Chrome(service = service_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.find_element(By.CSS_SELECTOR,".button").click()

file_input = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 5)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)
columnAttribute = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+columnAttribute+"-undefined']").text
print(actual_price)



