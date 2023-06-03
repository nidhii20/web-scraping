from selenium import webdriver
from selenium.webdriver.common.by import By


website= 'https://www.adamchoi.co.uk/overs/detailed'
path = "C:\\Users\\shubham\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver= webdriver.Chrome(path)
driver.get(website)

all_matches_button=driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()

matches=driver.find_elements(By.TAG_NAME,'tr')

date=[]
home_team=[]
score=[]
away_team=[]

for match in matches:
    date.append(match.find_element("xpath",'./td[1] ').text)
    home=match.find_element("xpath",'./td[2] ').text
    home_team.append(home)
    print(home)
    score.append(match.find_element("xpath",'./td[3] ').text)
    away_team.append(match.find_element("xpath",'./td[4] ').text)
