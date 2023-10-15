from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.get("https://www.gmail.com")
driver.find_element(By.XPATH, "//input[@name = 'identifier']").send_keys("abhilash@gmail.com")
driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()