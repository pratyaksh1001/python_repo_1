from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
data=driver.find_element(By.TAG_NAME,"p")
print(data.text)