from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sqlite3
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome(options=chrome_options)
con = sqlite3.connect("followers.db")
salt_user = []


def main():
    browser.get("https://www.instagram.com/")
    time.sleep(5)
    username = "YOUR_INSTAGRAM_USERNAME"
    password = "YOUR_INSTAGRAM_PASSWORD"
    login(username=username,password=password)
    time.sleep(5)
    profilePage()
    time.sleep(5)
    followerPage(con)
    
    
    con.close()


def login(username,password):
    user_area = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
    pass_area = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
    time.sleep(0.5)
    user_area.send_keys(username)
    time.sleep(0.5)
    pass_area.send_keys(password)
    time.sleep(0.5)
    pass_area.send_keys(Keys.ENTER)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR,".x1lliihq.x1n2onr6.x5n08af").click()

def scrollToUnderPage():
    lenOfPage = browser.execute_script("var divElement = document.getElementsByClassName('_aano')[0];divElement.scrollTop = divElement.scrollHeight;var lenOfDiv = divElement.scrollHeight;return lenOfDiv;")

    match = False

    while match == False:
        lastCount = lenOfPage
        time.sleep(1.7)
        lenOfPage = browser.execute_script("var divElement = document.getElementsByClassName('_aano')[0];divElement.scrollTop = divElement.scrollHeight;var lenOfDiv = divElement.scrollHeight;return lenOfDiv;")
        if lastCount == lenOfPage:
            match = True

def profilePage():
    profile_area = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div")
    time.sleep(0.5)
    profile_area.click()
    time.sleep(2)

def followerPage(con):
    follower_area = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
    time.sleep(0.5)
    follower_area.click()
    time.sleep(1)
    scrollToUnderPage()
    time.sleep(1)
    username_area = browser.find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")
    for users in username_area:
        salt_user.append(users.text)

    db_list = DBtoList()

    for last_user in db_list:
        if last_user in salt_user:
            continue
        else:
            print(f"{last_user} kişisi sizi takip etmiyor!!!")
            deleteDB(last_user)
                
    
        
    
    

    

        
def insertDB(con,value):
    try:
        cursor = con.cursor()
        sorgu = "INSERT INTO followers (username) VALUES (?)"
        cursor.execute(sorgu,(value,))
        con.commit()
        
    except sqlite3.IntegrityError as e:
        #print(f"ERROR:{e}\nTHIS IS A SAME VALUE.")
        pass

def checkDB(value):
    cursor = con.cursor()
    sorgu = "SELECT username FROM followers WHERE username = ?"
    cursor.execute(sorgu,(value,))
    result = cursor.fetchone()
    
    return len(result)

def deleteDB(value):
    cursor = con.cursor()
    sorgu = "DELETE FROM followers WHERE username = ?"
    cursor.execute(sorgu,(value,))
    con.commit()

def DBtoList():
    cursor = con.cursor()
    sorgu = "SELECT username FROM followers"
    cursor.execute(sorgu)
    rows = cursor.fetchall()
    data_list = []
    for row in rows:
        data_list.append(row[0])
    
    return data_list


def followingPage():
    following_area = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
    time.sleep(0.5)
    following_area.click()
    time.sleep(1)

def logout():
    logout_area = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a")
    time.sleep(0.5)
    logout_area.click()
    time.sleep(0.5)
    cikis = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]")
    time.sleep(0.5)
    cikis.click()
    time.sleep(0.5)
    browser.close()


if __name__ == "__main__":
    main()
