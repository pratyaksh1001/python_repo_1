from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Razer-DeathAdder-RZ01-02540100-R3M1-Essential-Optical/dp/B07F2GC4S9/")
price = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[5]/div[4]/div[14]/div/div/div[5]/div[1]/span[3]/span[2]/span[2]")
print(price.text)
driver.quit()