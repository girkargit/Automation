from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless") # Run testcase without invoking browser. At the backend
chrome_option.add_argument("--ignore-certificate-erros") # Handle ssl certificate errors.
service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj, options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.execute_script("window.scroll(0,500);") # Decide amount of scrolling page.
driver.execute_script("window.scroll(0,document.body.scrollHeight);")  # Scroll to bottom of the page.
driver.get_screenshot_as_file("screen.png")