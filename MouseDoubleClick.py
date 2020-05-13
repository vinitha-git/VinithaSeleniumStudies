from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

btn= driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

action = ActionChains(driver)
action.double_click(btn).perform()
