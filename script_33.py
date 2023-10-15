import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('ignore-certificate-errors')
# options.add_argument("headless")
service_obj = Service("/home/abhilash/abhilash_data/chrome/chromedriver")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5)

def login():
    driver.get('chrome://settings/')
    driver.maximize_window()
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
    driver.get("https://192.168.25.74/admin")
    driver.switch_to.frame("interfaces")
    driver.find_element(By.XPATH, "//input[@title = 'Enter Username']").send_keys("superuser")
    driver.find_element(By.XPATH, "//input[@title = 'Enter Password']").send_keys("wonderdream1")
    driver.find_element(By.XPATH, "//button[@name = 'submit']").click()
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation'+'confirmation popup to appear.')
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

def write_data_into_csv(data):
    file_path = "/home/abhilash/auto_tc/result.csv"
    with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

def clear_csv_file():
    filename = "/home/abhilash/auto_tc/6_result.csv"
    f = open(filename, "w+")
    f.close()

def remove_all_empty_value(xpath_lst):
    lst_new = []
    for i in xpath_lst:
        k = list(filter(None, i))
        lst_new.append(k)
    return lst_new

def convert_lst_to_str(file):
    lst = []
    for i in range(len(file)):
        lst.append(file[i][0])
    return lst

def edit_delete_action(xpath):
    xp = xpath.split('|')
    lst = driver.find_elements(By.XPATH, xp[2])
    for i in lst:
        txt = i.text
        if xp[1] in txt:
            time.sleep(0.4)
            i.find_element(By.XPATH, xp[3]).click()
            break

def alert():
    pop_up = driver.switch_to.alert
    pop_up.accept()

def cancle_alert():
    pop_up = driver.switch_to.alert
    pop_up.dismiss()

def time_sleep():
    time.sleep(2)

def scrolling():
    driver.execute_script("window.scrollBy(0,500);")

def switch_window():
    window = driver.window_handles
    driver.switch_to.window(window[1])

def back_to_window():
    window = driver.window_handles
    driver.switch_to.window(window[0])
    driver.switch_to.frame("right")

def date_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    lst = [dt_string, "FireWall version 4.32"]
    return lst

def run_testcase():
    file = '/home/abhilash/auto_tc/test_path.csv'
    xpath_lst = read_data_from_csv(file)
    xpath_file_path = remove_all_empty_value(xpath_lst)
    csv_path = convert_lst_to_str(xpath_file_path)
    for path in csv_path:
        if path == "/home/abhilash/auto_tc/host_add.csv":
            clear_csv_file()
            op = date_time()
            write_data_into_csv([op, ["Input action", "Result"]])
        xpath_tab = read_data_from_csv(path)
        xpath_new = remove_all_empty_value(xpath_tab)
        driver.switch_to.frame("left")
        driver.find_element(By.XPATH, xpath_new[0][0]).click()
        if xpath_new[1][0] == "no tab":
            pass
        else:
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

                elif value.split('|')[0] == "edit" or value.split('|')[0] == "delete" or value.split('|')[0] == "clone":
                    edit_delete_action(value)

                elif value == "alert":
                    alert()

                elif value == "cancel":
                    cancle_alert()

                elif value == "switch_window":
                    switch_window()

                elif value == "scroll":
                    scrolling()

                elif value == "sleep":
                    time_sleep()

                elif value == "right_window":
                    back_to_window()

                elif value.split('|')[0]== "click":
                    if 'OK' in value:
                        info = driver.find_element(By.XPATH, "(//td[@id='success_msg'])").text
                        status = "fail"
                        if "successfully" or "Successfully" in info:
                            status = "pass"
                        write_data_into_csv([[xpath[0], status]])
                    time.sleep(0.4)
                    driver.find_element(By.XPATH, value.split('|')[1]).click()

                elif value.split('|')[0] == "select":
                    op = value.split('|')
                    dropdown = Select(driver.find_element(By.XPATH, op[1]))
                    dropdown.select_by_value(op[2])

                else:
                    point = value.split('|')
                    driver.find_element(By.XPATH, point[1]).send_keys(point[2])
                    time.sleep(0.2)
        driver.switch_to.default_content()

login()
run_testcase()
