import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.implicitly_wait(5)# Implicit wait
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
vegitable_lst = driver.find_elements(By.XPATH, "//table[@class='table table-bordered']/tbody/tr/td[1]")
print(len(vegitable_lst))
lst = []

for i in vegitable_lst:
    lst.append(i.text)
print(lst)
original = lst.copy()
lst.sort()
assert lst == original