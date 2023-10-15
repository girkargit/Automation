from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service = service_obj )
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
print(driver.title)
print(driver.current_url)
driver.close()
