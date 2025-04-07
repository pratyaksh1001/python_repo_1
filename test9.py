from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from test10 import gemini

browser=webdriver.Chrome()
browser.get('https://www.netacad.com/')
time.sleep(5)
login=browser.find_element(By.XPATH,value="/html/body/div[2]/div[1]/nav/div/div/div[2]/div[6]/button")
login.click()
time.sleep(3)
email=browser.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div/div[2]/div/div[1]/div[1]/form/div[1]/div/input")
email.send_keys("pratyaksh0856.be23@chitkara.edu.in")
login=browser.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div/div[2]/div/div[1]/div[1]/form/div[3]/input[2]")
login.click()
time.sleep(3)
password=browser.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div/div[2]/div/div[1]/div[1]/form/div[2]/div/input")
password.send_keys("Pratyaksh_102080")
login=browser.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div/div[2]/div/div[1]/div[1]/form/div[4]/input[2]")
login.click()
time.sleep(5)
course=browser.find_element(by=By.XPATH,value="/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/div[1]/div/button")
course.click()
time.sleep(5)