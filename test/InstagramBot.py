from selenium import webdriver
from time import sleep
from password import PW


class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username =username
        self.driver.get('https://instagram.com')
        sleep(4)
        # //a is a link
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        # sleep(10)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()





my_bot = Instabot('anisacurlz', PW)
# my_bot.get_unfollowers
