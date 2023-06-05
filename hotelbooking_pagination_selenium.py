from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website='https://www.booking.com/searchresults.html?ss=New+Delhi%2C+India&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Atap-KMGwAIB0gIkMmViYjI1ZjctODMxZS00YTFlLThiNTAtODI2YmFlNzgzZjBi2AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2106102&dest_type=city&checkin=2023-06-05&checkout=2023-06-06&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
path="C:\\Users\\shubham\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(website)

#pagination
pagination=driver.find_element(By.XPATH,'//div[contains(@class,"a8b500abde")]')
pages=pagination.find_elements(By.XPATH,'.//button[contains(@class,"fc63351294 f9c5690c58")]')
last_page=int(pages[-2].text)

current_page=1


name=[]
rate=[]

while current_page<=last_page:
    time.sleep(3)
    noice=driver.find_element(By.CLASS_NAME,'d4924c9e74')
    lists=noice.find_elements(By.XPATH,'.//div[contains(@class,"d20f4628d0")]')


    for element in lists:
        N=element.find_element(By.XPATH,'.//div[contains(@class,"fcab3ed991 a23c043802")]').text
        name.append(N)
        #print(N)
        R=element.find_element(By.XPATH,'.//span[contains(@class,"fcab3ed991 fbd1d3018c e729ed5ab6")]').text
        rate.append(R)
        #print(R)

    current_page=current_page+1   

    try:
        next_page=driver.find_element(By.XPATH,'//div[contains(@class,"f32a99c8d1 f78c3700d2")]') 
        next_page.click()
    except:
        pass

driver.quit()

df_booking=pd.DataFrame({'Name':name,'Rate':rate})
df_booking.to_csv('Booking.csv',index=False)
