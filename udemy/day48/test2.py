from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detatch",True)
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys("razer deathadder")
search.submit()
main_section=driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]")
