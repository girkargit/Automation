from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--ignore-certificate-errors") # certificate error
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# //a[contains(@href,'shop')] == xpath
# a[href*='shop'] == css  This are rdegular expression
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
lst = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for i in lst:
    if i.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
        i.find_element(By.XPATH, "div/button").click()
        break
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul[1]/li")))
driver.find_element(By.XPATH, "//div[@class='suggestions']/ul[1]/li").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']/label").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
txt = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in txt
driver.close()
