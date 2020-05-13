from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path ="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe");
driver.get("http://newtours.demoaut.com/")
print(driver.title);
print(driver.current_url);
print(driver.page_source);
driver.close();
