from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert


URL = "http://192.168.1.1/index.asp"  # YOUR ROUTER IP ADDRESS
ID = "YOUR ID"  # YOUR LOGIN ID
PASSWORD = "YOUR PASSWORD"  # YOUR PASSWORD


driver_path = "driver path"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)

id = driver.find_element_by_xpath("login_user")
pwd = driver.find_element_by_name("login_pass")

id.send_keys(ID)
pwd.send_keys(PASSWORD)
submit = driver.find_element_by_name("login")
submit.click()

time.sleep(1)
advanced = driver.find_element_by_xpath(
    '//*[@id="box_header"]/center/input[2]')
advanced.click()

time.sleep(1)
maintainence = driver.find_element_by_xpath('//*[@id="Tools_topnav"]')
maintainence.click()


save_settings = driver.find_element_by_xpath(
    '//*[@id="Tools_subnav"]/li[2]/div/a')
save_settings.click()


reboot = driver.find_element_by_xpath('//*[@id="btn_reboot"]')
reboot.click()

# Accept the Js alert pop up

time.sleep(1)
Alert(driver).accept()
