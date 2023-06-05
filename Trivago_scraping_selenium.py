from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web='https://www.trivago.in/en-IN/srl?themeId=280&search=200-64981&sem_keyword=trivago&sem_creativeid=598703244708&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=&sem_param1=&sem_param2=&sem_campaignid=12417347003&sem_adgroupid=118398776556&sem_targetid=kwd-5593367084&sem_location=9061708&cipc=br&cip=9119000005&gclid=Cj0KCQjwj_ajBhCqARIsAA37s0ybT-RGZCasxIDnuuif5ORsA2X_XhQlVbro5PEE99sxkcSYZsgxiToaAlYPEALw_wcB'
path="C:\\Users\\shubham\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(web)

contains=driver.find_element(By.XPATH,'//div[contains(@class,"relative min-h-screen pt-1")]')
lists=contains.find_elements(By.XPATH,'.//div[contains(@class,"bg-white rounded-md shadow-nux-15")]')

Heading=[]
Price=[]

for item in lists:
    heading=item.find_element(By.XPATH,'.//h2[contains(@class,"text-heading-m ItemNameSection_nameWithFav__HXgUl")]').text
    Heading.append(heading)
    price=item.find_element(By.XPATH,'.//div[contains(@class,"flex align-bottom flex-wrap")]').text
    Price.append(price)
    print("heading:",heading)
    print("price:",price)

driver.quit()

df_hotel=pd.DataFrame({'Heading':Heading,'Price':Price})
df_hotel.to_csv('Hotels.csv',index=False)
