from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

web= "https://www.railyatri.in/booking/trains-between-stations?device_type_id=6&from_code=NDLS&from_name=NEW+DELHI+&journey_date=04-06-2023&src=tbs&to_code=BSB&to_name=VARANASI+JN+&user_id=-1685866195&user_token=61685866195&utm_source=tt_dwebhome_search"
path= "C:\\Users\\shubham\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()


container= driver.find_element(By.ID,'tbs-main')
trains=container.find_elements(By.XPATH,'.//div[contains(@class,"tbs-main-row")]')

train_name=[]
train_timing=[]

for train in trains:
    train_name.append(train.find_element(By.XPATH,'.//div[contains(@class,"namePart")]').text)
    train_timing.append(train.find_element(By.XPATH,'.//div[contains(@class,"TravelTimeInfo")]').text)

driver.quit()

df_trains=pd.DataFrame({'Train_name':train_name,'Train_timings':train_timing})
df_trains.to_csv('Trains.csv',index=False)
