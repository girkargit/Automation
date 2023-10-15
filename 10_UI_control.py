from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkbox = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
for check in checkbox:
    if check.get_attribute("value") == 'option2':
        check.click()
        assert check.is_selected()
        break
radio = driver.find_elements(By.XPATH, "//input[@type = 'radio']")
# for button in radio:
#     if button.get_attribute("value") == "radio2":
#         button.click()
#         break

# class methode turn into css locator used dot befor class attribute
radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobutton[2].click() # index value
assert radiobutton[2].is_selected()
assert driver.find_element(By.XPATH, "//input[@id = 'displayed-text']").is_displayed() # show if displed or not
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.XPATH, "//input[@id = 'displayed-text']").is_displayed() # show if displed or not
