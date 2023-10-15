import csv
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class GajFirewallTest:

    def __init__(self):

        self.__main_csv_file = "/home/abhilash/Desktop/automation/Automstion_Script/20190102/Firewall/Firewall_test.csv"
        self.__fw_admin_url = "https://192.168.2.107/admin/index.html"
        self.__test_report_file_path = "/home/abhilash/Desktop/automation/Automstion_Script/Test_report.csv"
        self.__all_test_cases = 0
        self.__test_case_pass = 0
        self.__test_case_fail = 0

    def get_data_from_csv_file(self, csv_file):

        fp = open(csv_file, 'r')
        csv_reader = csv.reader(fp)
        data = list(csv_reader)
        fp.close()
        return data

    def login_to_firewall(self):

        self.driver = webdriver.Chrome(executable_path='/home/abhilash/Desktop/ChromeDriver/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(self.__fw_admin_url)
        self.driver.switch_to_frame(self.driver.find_element_by_name(
            "interfaces"))
        self.driver.find_element_by_id("uname").send_keys("abhi")
        self.driver.find_element_by_id("passwd").send_keys("abhi")
        self.driver.find_element_by_id("submitbtn").click()
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(self.driver.find_element_by_name('top'))
        self.driver.find_element_by_xpath('//*[@id="sidebar_open"]').click()
        self.driver.switch_to_default_content()

    def test_all_tabs(self):

        fp = open(self.__test_report_file_path, 'w')
        self.__test_report_file_writer = csv.writer(fp)
        self.__test_report_file_writer.writerow(["Test Case ID", "Test Case " \
                                                                 "Name", "Status", "Expected Result", "Actual Result"])
        self.login_to_firewall()
        main_csv_file_info = self.get_data_from_csv_file(self.__main_csv_file)
        # print(main_csv_file_info)
        # print("hi")

        for tab_details in main_csv_file_info[1:]:
            tab_name, csv_file_path = tab_details
            # print(tab_details)
            # print("hi")

            self.test_tab(tab_name, csv_file_path)
        self.__test_report_file_writer.writerow(["Total: %d" \
                                                 % (self.__all_test_cases), "Pass: %d" \
                                                 % (self.__test_case_pass), "Fail: %d" \
                                                 % (self.__test_case_fail)])
        self.logout()
        fp.close()

    def test_tab(self, tab_name, csv_file_path):
        test_tab_info = self.get_data_from_csv_file(csv_file_path)
        print(test_tab_info)
        print(1)
        for action_details in test_tab_info[1:]:
            action, test_data_file = action_details
            print(action_details)
            self.run_all_test_cases(test_data_file)

    def navigate_to_tab(self, navigation_frame, navigation_xpath):
        if navigation_frame:
            self.driver.switch_to_frame(self.driver.find_element_by_name(navigation_frame))

        for xpath in navigation_xpath:
            self.driver.find_element_by_xpath(xpath).click()
        self.driver.switch_to_default_content()

    def goto_tab(self, tab_frame_name, tab_xpath):

        self.driver.switch_to_frame(self.driver.find_element_by_name(
            tab_frame_name))
        self.driver.find_element_by_xpath(tab_xpath).click()
        self.driver.switch_to_default_content()

    def perform_pre_action(self, pre_action_frame, pre_action_xpath):

        import time
        time.sleep(10)

        if pre_action_frame:
            self.driver.switch_to_frame(self.driver.find_element_by_name(
                pre_action_frame))
        after_window = ''
        window_flag = False
        before_window = self.driver.window_handles[0]
        for xpath in pre_action_xpath:
            if xpath:
                self.driver.find_element_by_xpath(xpath).click()
                if window_flag:
                    after_window = ''
                    window_flag = False
                    self.driver.switch_to_window(before_window)
                    if pre_action_frame:
                        self.driver.switch_to_frame(self.driver. \
                                                    find_element_by_name(pre_action_frame))
                if len(self.driver.window_handles) > 1:
                    after_window = self.driver.window_handles[1]
                if after_window:
                    window_flag = True
                    self.driver.switch_to_window(after_window)
            else:
                pass

    def run_test_case(self, input_xpath, input_data):

        for i in range(len(input_xpath)):
            self.driver.find_element_by_xpath(input_xpath[i]).send_keys(
                keys.Keys.CONTROL + "a" + keys.Keys.CLEAR)
            self.driver.find_element_by_xpath(input_xpath[i]).send_keys(
                input_data[i])

    def perform_post_action(self, post_action_xpath):

        for xpath in post_action_xpath:
            self.driver.find_element_by_xpath(xpath).click()

    def get_alert(self):

        try:
            Alert = self.driver.switch_to_alert()
            Alert.accept()
        except:
            pass

    def get_alert_text(self):

        try:
            Alert = self.driver.switch_to_alert()
            Alert_text = str(Alert.text)
            Alert.accept()
            return Alert_text
        except:
            return ""

    def get_actual_result(self, actual_result_xpath):

        alert_message = self.get_alert_text()
        if alert_message:
            return alert_message
        return str(self.driver.find_element_by_xpath(actual_result_xpath) \
                   .text)

    def compare_actual_result(self, actual_result_xpath, exp_result,
                              test_case_id, test_case_name):

        if self.check_exists_by_xpath(actual_result_xpath):
            actual_result = self.get_actual_result(actual_result_xpath)
        else:
            actual_result = ""
        if actual_result == exp_result:
            test_status = "PASS"
            self.__test_case_pass += 1
        else:
            test_status = "FAIL"
            self.__test_case_fail += 1
        self.__all_test_cases += 1
        self.__test_report_file_writer.writerow([test_case_id, test_case_name,
                                                 test_status, exp_result, actual_result])

    def run_all_test_cases(self, test_data_file):

        test_data_info = self.get_data_from_csv_file(test_data_file)
        tmp_data = test_data_info[1][0].split('|', 1)
        navigation_frame = tmp_data[0]
        navigation_xpath = tmp_data[1].split(',')
        tab_frame_name, tab_xpath = test_data_info[1][1].split('|', 1)
        temp_data = test_data_info[1][2].split('|', 1)
        pre_action_frame = temp_data[0]
        pre_action_xpath = temp_data[1].split(',')
        input_xpath = test_data_info[1][3].split(',')
        post_action_xpath = test_data_info[1][4].split(',')
        self.navigate_to_tab(navigation_frame, navigation_xpath)
        for test_case in test_data_info[3:]:
            test_case_id = test_case[0]
            actual_result_xpath = test_case[1]
            test_case_name = test_case[2]
            exp_result = test_case[3]
            input_data = test_case[4:]
            self.goto_tab(tab_frame_name, tab_xpath)
            self.perform_pre_action(pre_action_frame, pre_action_xpath)
            self.get_alert()
            self.run_test_case(input_xpath, input_data)
            self.perform_post_action(post_action_xpath)
            self.compare_actual_result(actual_result_xpath, exp_result,
                                       test_case_id, test_case_name)
            self.driver.switch_to_default_content()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def logout(self):

        self.driver.switch_to_frame(self.driver.find_element_by_name("left"))
        self.driver.find_element_by_xpath(".//*[@id='accordion_logout']/li/" \
                                          "div").click()
        self.get_alert()


gsfw_test_obj = GajFirewallTest()
gsfw_test_obj.test_all_tabs()


