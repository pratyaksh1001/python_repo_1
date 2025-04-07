from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"
driver = webdriver.Chrome()
driver.get(url)
data = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
for i in data:
    print(i.text)
    