from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/din--33535"

browser.get(url=url)

xpath = "/html/body/div[2]/div[2]/div[2]/section/div[1]/ul/li[1]/div[1]" 

time.sleep(10)
i = 0
while i < 50:
    contents = browser.find_elements(By.CSS_SELECTOR,".content")
    time.sleep(0.5)
    authors = browser.find_elements(By.CSS_SELECTOR,".entry-author")
    for element,author in zip(contents,authors):
        f = open("diniyorumlar.txt",mode="a",encoding="utf-8")
        text = f"***********************************************\n{element.text}\nYazinin Sahibi: {author.text}\n***********************************************" 
        f.write(text)
        f.close()
    i += 1
    browser.find_element(By.CSS_SELECTOR,".next").click()
    time.sleep(5)
    

browser.close()