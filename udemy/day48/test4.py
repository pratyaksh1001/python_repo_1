from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detatch",False)
driver=webdriver.Chrome()
driver.get("https://google.com")
search=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
x=input("enter the thing you want to search on wikipedia: ")
search.send_keys(x+" wikipedia")
search.submit()
"""link=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
link.click()"""
time.sleep(5)
link=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
link.click()