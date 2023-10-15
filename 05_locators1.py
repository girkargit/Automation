from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("test@test.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("test123")
# driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("test123")
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("test123")
