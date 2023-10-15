from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\chrome_driver\chromedriver")
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=options , service= service_obj)
driver.get('https://192.168.2.107/admin')
driver.implicitly_wait(2)
driver.switch_to.frame("interfaces")
driver.find_element(By.XPATH , "//form/div[1]/input").send_keys("abhi")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("abhi")
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()