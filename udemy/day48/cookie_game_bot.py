# needs to be run multiple times as many times the cookie click fails

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
UPG=1
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
lang=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
lang.click()
cookie=driver.find_element(By.XPATH,"/html/body/div/div[2]/div[15]/div[8]/button")
time.sleep(2)
got_it=driver.find_element(By.XPATH,"/html/body/div[1]/div/a[1]")
got_it.click()
time.sleep(2)
for i in range(20):
    time.sleep(0.5)
    cookie.click()


def fun1():
    global UPG
    try:
        while True:
            print(UPG)
            if UPG % 10 != 0:
                tools = driver.find_elements(By.CLASS_NAME, "enabled")
                tools = tools[::-1]
                for i in tools:
                    print(i.text.split("\n"))
                    if len(i.text.split("\n")) == 1:
                        continue
                    elif len(i.text.split("\n")) == 2:
                        i.click()
                    elif len(i.text.split("\n")) == 3:
                        i.click()

                UPG += 1
            else:
                upgrades = driver.find_elements(By.CLASS_NAME, "upgrade")
                upgrades = upgrades[::-1]
                for i in upgrades:
                    print(i.text.split("\n"))
                    if len(i.text.split("\n")) > 1:
                        i.click()
                    else:
                        continue
                UPG = 1
            time.sleep(10)
    except:
        fun1()
fun1()