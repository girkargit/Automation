from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# id, Xpath, CSS selecctor, Class name, name, link text
# driver.find_element(By.NAME, "name").send_keys("test")
driver.find_element(By.NAME, "email").send_keys("test.test.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test@123")
driver.find_element(By.ID, "exampleCheck1").click() # click action

# xpath = //tagnaname[@attribute = 'value'] --> //input[@type = 'submit']
# CSS = tagnaname[attribute = 'value'] #id, .classname

driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("test")
driver.find_element(By. CSS_SELECTOR, "#inlineRadio1").click()

# *******   Static drop down *****************
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
# dropdown.deselect_by_visible_text("Female")

driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("task")



