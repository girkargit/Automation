from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('ignore-certificate-errors')
service_obj = Service("/home/abhilash/Desktop/chrome/chromedriver")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(2)

def login():
    driver.get("https://192.168.25.51/admin")
    driver.switch_to.frame("interfaces")
    driver.find_element(By.XPATH, "//input[@title = 'Enter Username']").send_keys("test")
    driver.find_element(By.XPATH, "//input[@title = 'Enter Password']").send_keys("test")
    driver.find_element(By.XPATH, "//button[@name = 'submit']").click()
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation '+'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print("no alert")
    driver.switch_to.frame("top")
    driver.find_element(By.XPATH, "//button[@id = 'sidebar_open']").click()
    driver.switch_to.default_content()

def read_data_from_csv(file_name):
    lst = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return lst

def write_data_into_csv(data, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

def remove_all_empty_value(xpath_lst):
    lst_new = []
    for i in xpath_lst:
        k = list(filter(None, i))
        lst_new.append(k)
    return lst_new

def edit_delete_action(xpath):
    xp = xpath.split('|')
    lst = driver.find_elements(By.XPATH, xp[2])
    for i in lst:
        txt = i.text
        if xp[1] in txt:
            i.find_element(By.XPATH, xp[3]).click()
            break

def alert():
    pop_up = driver.switch_to.alert
    pop_up.accept()

def switch_window():
    window = driver.window_handles
    driver.switch_to.window(window[1])

def back_to_window():
    window = driver.window_handles
    driver.switch_to.window(window[0])
    driver.switch_to.frame("right")

def run_testcase():
    result = [["host_ID", "host_IP", "result"]]
    file_path= '/home/abhilash/auto_tc/guest_user.csv'
    xpath_lst = read_data_from_csv(file_path)
    xpath_new = remove_all_empty_value(xpath_lst)
    driver.switch_to.frame("left")
    driver.find_element(By.XPATH, xpath_new[0][0]).click()
    driver.find_element(By.XPATH, xpath_new[1][0]).click()
    driver.switch_to.default_content()
    driver.switch_to.frame("tabs")
    driver.find_element(By.XPATH, xpath_new[2][0]).click()
    driver.switch_to.default_content()
    driver.switch_to.frame("right")
    for xpath in xpath_new[4:len(xpath_new)-1]:
        for value in xpath[1:]:
            if value.split('|')[0] == "search":
                data = value.split('|')
                driver.find_element(By.XPATH, data[1]).send_keys(data[2])

            elif value.split('|')[0] == "edit" or value.split('|')[0] == "delete":
                edit_delete_action(value)

            elif value == "alert":
                alert()

            elif value == "switch_window":
                switch_window()

            elif value == "right_window":
                back_to_window()

            elif value.split('|')[0] == "click":
                if 'OK' in value:
                    info = driver.find_element(By.XPATH, "(//td[@id='success_msg'])").text
                    A = "fail"
                    if "successfully" in info:
                        A = "pass"
                    result.append([xpath[0], A])
                driver.find_element(By.XPATH, value.split('|')[1]).click()

            elif value.split('|')[0] == "select":
                op = value.split('|')
                dropdown = Select(driver.find_element(By.XPATH, op[1]))
                dropdown.select_by_value(op[2])
            else:
                point = value.split('|')
                driver.find_element(By.XPATH, point[1]).send_keys(point[2])
    write_data_into_csv(result, xpath_new[-1][0])

login()
run_testcase()

