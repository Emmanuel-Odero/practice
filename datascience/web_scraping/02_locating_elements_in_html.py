from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

#get the site title then close the browser
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(keys.RETURN)
driver.quit()