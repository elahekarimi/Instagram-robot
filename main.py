from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
CHROME_DRIVER_PATH = "D:\chromDriver\chromedriver.exe"


class InstaFollower:
    def __init__(self, chrom_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrom_driver_path)

    def login(self):
        time.sleep(2)
        self.driver.get("https://www.instagram.com/")
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys("emailmypython@gmail.com")
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys('890350455')
        time.sleep(2)
        log_In = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        log_In.click()

    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{'mes_delicieuses_creations'}")
        time.sleep(2)
        follower = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        follower.click()
        time.sleep(2)
        # modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()



# time.sleep(2)
# box = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
# box.send_keys("mes_delicieuses_creations")



