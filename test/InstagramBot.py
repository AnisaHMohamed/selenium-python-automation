from selenium import webdriver
from time import sleep
from password import PW


class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get('https://instagram.com')
        sleep(2)
        # //a is a link
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        # people who reposted or shared your poara
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
        # suggestions = self.driver.find_element_by_xpath("//h4[contains(text(), Suggestions)]")
        # self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
        sleep(1)
        ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight);
    return arguments[0].scrollHeight;""", scroll_box)
        links = self.driver.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

my_bot = Instabot('anisacurlz', PW)
my_bot.get_unfollowers()
