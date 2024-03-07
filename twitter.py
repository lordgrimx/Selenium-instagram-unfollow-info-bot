from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

tw_mail= "yoyamep975@hidelux.com"
tw_pass = "asker123"
tw_usurname= "DHesabl84147"

browser = webdriver.Chrome()

browser.get("https://twitter.com/i/flow/login")

time.sleep(5)

mail=browser.find_element(By.CSS_SELECTOR,".r-1dz5y72")

mail.click()
time.sleep(2)
mail.send_keys(tw_mail)
time.sleep(2)
mail.send_keys(Keys.ENTER)
time.sleep(4)

usurname = browser.find_element(By.CSS_SELECTOR,".r-30o5oe .r-1dz5y72 .r-13qz1uu")

usurname.click()
time.sleep(2)
usurname.send_keys(tw_usurname)
time.sleep(2)
usurname.send_keys(Keys.ENTER)
time.sleep(2)


