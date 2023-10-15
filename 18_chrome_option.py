from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized") # maximized the chrome window
chrome_option.add_argument("headless") # code run in background
chrome_option.add_argument("--ignore-certificate-errors") # certificate error
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj, options= chrome_option )
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)