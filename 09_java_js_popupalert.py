from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@name = 'enter-name']").send_keys("test")
driver.find_element(By.XPATH, "//input[@id = 'alertbtn']").click()
alert = driver.switch_to.alert
k = alert.text
alert.accept() # for click on ok

# driver.find_element(By.ID, "confirmbtn").click()
# alert1 = driver.switch_to.alert
# alert1.dismiss() # for click in cancel