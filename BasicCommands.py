from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html");

print (driver.title)

print (driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
#driver.close()
#driver.quit()