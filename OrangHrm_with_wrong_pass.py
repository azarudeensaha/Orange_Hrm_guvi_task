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
        self.invalid_password = "invalidpassword"
        self.username_loc_name_tag = "username"
        self.password_loc_name_tag = "password"

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        actions = ActionChains(self.driver)
        sleep(5)

    def input_credentials(self):
        username_webelement = self.driver.find_element(By.NAME, self.username_loc_name_tag)
        username_webelement.send_keys(self.username)

        password_webelement = self.driver.find_element(By.NAME, self.password_loc_name_tag)
        password_webelement.send_keys(self.invalid_password)

        sleep(2)
        login_path_xpath = '//button[@type="submit"]'
        login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        login_button_webelement.click()
        title_1 = self.driver.title
        print(title_1)
        sleep(3)
        self.driver.close()


obj = OrangeHrm()
obj.browse()
obj.input_credentials()