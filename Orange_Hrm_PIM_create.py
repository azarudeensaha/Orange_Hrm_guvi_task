from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)



class OrangeHrm:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome(options=options)
        self.username = "Admin"
        self.password = "admin123"
        self.username_loc_name_tag = "username"
        self.password_loc_name_tag = "password"
        self.pim_menu_page2="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
        self.add_emp='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        self.emp_firstname_locater = 'firstName'
        self.emp_lastname_locater = 'lastName'
        self.first_name = 'Azarudeen'
        self.last_name = 's'
        self.emp_id_locator="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
        self.emp_id="1995"

        self.emp_save_path = '//button[@type="submit"]'
        self.logging_out_menu = '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]'
        self.logging_out = "//a[text()='Logout']"



    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        actions = ActionChains(self.driver)
        sleep(5)

    def input_credentials(self):
        username_webelement = self.driver.find_element(By.NAME, self.username_loc_name_tag)
        username_webelement.send_keys(self.username)

        password_webelement = self.driver.find_element(By.NAME, self.password_loc_name_tag)
        password_webelement.send_keys(self.password)

        sleep(2)
        login_path_xpath = '//button[@type="submit"]'
        login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        login_button_webelement.click()
        title_1 = self.driver.title
        print(title_1)
        sleep(3)

    def pim_page(self):
        pim_menu_element = self.driver.find_element(By.XPATH, self.pim_menu_page2)
        pim_menu_element.click()
        sleep(3)

    def add_new_emp(self):
        emp_page = self.driver.find_element(By.XPATH, self.add_emp)
        emp_page.click()
        sleep(5)
        emp_first_name = self.driver.find_element(By.NAME, self.emp_firstname_locater)
        emp_first_name.send_keys(self.first_name)
        sleep(3)
        emp_last_name = self.driver.find_element(By.NAME, self.emp_lastname_locater)
        emp_last_name.send_keys(self.last_name)
        sleep(3)
        emp_id_num=self.driver.find_element(By.XPATH, self.emp_id_locator)
        emp_id_num.send_keys(self.emp_id)

        new_emp_submit = self.driver.find_element(By.XPATH, self.emp_save_path)
        new_emp_submit.click()
        sleep(5)



obj = OrangeHrm()
obj.browse()
obj.input_credentials()
obj.pim_page()
sleep(5)
obj.add_new_emp()



'''
        logout_menu_webelement = self.driver.find_element(By.XPATH, self.logging_out_menu)
        logout_menu_webelement.click()
        sleep(3)

        actions_obj = ActionChains(self.driver)
        logout_webelement = self.driver.find_element(By.XPATH, self.logging_out)
        # no Action chain is successfull without perform function
        logout_webelement.click()
        sleep(5)
        
'''
