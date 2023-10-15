from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('ignore-certificate-errors')
service_obj = Service("/home/abhilash/Desktop/chrome/chromedriver")
driver = webdriver.Chrome(options=options, service=service_obj)
def login():
    driver.get("https://192.168.25.51/admin")
    driver.switch_to.frame("interfaces")
    driver.find_element(By.XPATH, "//input[@title = 'Enter Username']").send_keys("test")
    driver.find_element(By.XPATH, "//input[@title = 'Enter Password']").send_keys("test")
    driver.find_element(By.XPATH, "//button[@name = 'submit']").click()
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

def run_testcase():
    result = [["host_ID", "host_IP", "result"]]
    file = 'C:\\test_case\host_tab.csv'
    xpath_lst = read_data_from_csv(file)
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
        for value in xpath:
            if value.split('|')[0]== "click":
                if 'OK' in value:
                    info = driver.find_element(By.XPATH, "(//td[@id='success_msg'])").text
                    id = xpath[1].split('|')[2]
                    ip = xpath[2].split('|')[2]
                    A = "fail"
                    if "successfully" in info:
                        A = "pass"
                    result.append([id, ip, A])
                driver.find_element(By.XPATH, value).click()
            elif value.split('|')[0] == "select":
                op = value.split('|')
                dropdown = Select(driver.find_element(By.XPATH, op[1]))
                dropdown.select_by_value(op[2])
            else:
                point = value.split('|')
                driver.find_element(By.XPATH, point[1]).send_keys(point[2])
    write_data_into_csv(result,xpath_new[-1][0])

login()
run_testcase()