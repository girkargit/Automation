from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frame.")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)

