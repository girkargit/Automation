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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type = 'search']").send_keys("ber")
time.sleep(2)
accepted = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual = []
results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(results)
assert count > 0
for result in results:
    actual.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click() # Chaining of web element
assert accepted == actual
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# Sum validation
# price = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
price = driver.find_elements(By.XPATH,"//table[@id='productCartTables']/tbody/tr/td[5]//p[@class = 'amount']")
sum = 0
for p in price:
    sum = sum + int(p.text)
print(sum)
amt = int(driver.find_element(By.XPATH,"//span[@class= 'totAmt']").text)
assert sum == amt
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10) # Explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
disc = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert amt > disc