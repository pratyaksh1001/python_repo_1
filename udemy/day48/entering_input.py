from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
inp1=driver.find_element(By.XPATH,value='/html/body/form/input[1]')
inp1.send_keys("hello world",Keys.ENTER)
time.sleep(1)
inp2=driver.find_element(By.XPATH,value='/html/body/form/input[2]')
inp2.send_keys("how are you",Keys.ENTER)
time.sleep(1)
inp3=driver.find_element(By.XPATH,value='/html/body/form/input[3]')
inp3.send_keys("jydkuglbf@teferv.com",Keys.ENTER)
time.sleep(5)
driver.quit()