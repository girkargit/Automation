import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service = service_obj )
driver.implicitly_wait(10)
driver.get('chrome://settings/')
driver.maximize_window()
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.7);')

driver.get("https://amazon.in") # amazon url
product_name = "div[1]//span[@class='a-size-medium a-color-base a-text-normal']"
main_path = "//div[@class='a-section']/div/div[2]/div/div"

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("samsung")
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']"))
dropdown.select_by_value("search-alias=aps")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
product_lst = driver.find_elements(By.XPATH, main_path)
final_lst = []
for i in range(len(product_lst)):
    if i <= 4:
        k = product_lst[i].find_element(By.XPATH, product_name).text
        y = product_lst[i].find_element(By.CLASS_NAME, "a-price-whole").text
        # print(k, "-->>", y)
        final_lst.append("product name :- %s | price :- %s" %(k, y))

with open("file.text", "w") as fp:
    for i in final_lst:
        fp.write(i + "\n")






