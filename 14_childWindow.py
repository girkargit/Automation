from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
window = driver.window_handles
print("Open window list = ", window) # on 0th index parent window is stored and onwards
driver.switch_to.window(window[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() # closed child window
driver.switch_to.window(window[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


