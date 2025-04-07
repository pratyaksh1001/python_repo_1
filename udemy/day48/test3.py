from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options=webdriver.ChromeOptions()
#chrome_options.add_experimental_option("detatch",False)
driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/United_States")
data=driver.find_elements(By.TAG_NAME,"p")
data=list(data[4:])
file=open("USA_wiki.txt","a+",encoding="utf8")
for i in data:
    file.write(i.text+"\n")
file.close()