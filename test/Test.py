from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://google.com')
driver.find_element_by_name("q").send_keys("Anisa Mohamed")
# driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[3]/center/input[1]").click()
driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)

# driver.set_page_load_timeout(10)
time.sleep(4)
driver.quit()