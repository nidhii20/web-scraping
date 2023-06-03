from selenium import webdriver

website= 'https://www.adamchoi.co.uk/overs/detailed'
path = "C:\\Users\\shubham\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver= webdriver.Chrome(path)
driver.get(website)

all_matches_button=driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()
