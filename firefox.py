from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\\firefox_driver\geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")