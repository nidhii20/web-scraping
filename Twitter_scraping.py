from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website="https://twitter.com/"
path="C:\\Users\\shubham\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(website)
#driver.maximize_window()

login=driver.find_element(By.XPATH,'//a[@href="/login"]')
login.click()
time.sleep(2)

username_box=driver.find_element(By.XPATH,'//div[contains(@class,"css-1dbjc4n r-ywje51 r-nllxps")]')
username=username_box.find_element(By.XPATH,'.//div[@class="css-1dbjc4n r-16y2uox r-1wbh5a2"]')
username.send_keys("riyaaa202002@gmail.com")    
next=username_box.find_element(By.XPATH,'.//div[contains(@class,"css-18t94o4 css-1dbjc4n r-s")]')
next.click()

login_page=driver.find_element(By.XPATH,'//div[contains(@class,"css-1dbjc4n r-16y2uox r-1wbh5a2 r-1j")]')
password=login_page.find_element(By.XPATH,'.//label[contains(@class,"css-1dbjc4n r-1e")]')
password.send_keys("surbhi20")
login_button=login_page.find_element(By.XPATH,'.//div[contains(@class,"css-1dbjc4n r-sdzlij r-1p")]')
login_button.click()
