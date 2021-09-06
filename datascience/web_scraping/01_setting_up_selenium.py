from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://int.soccerway.com/")

#get the site title then close the browser
print(driver.title)
driver.quit()