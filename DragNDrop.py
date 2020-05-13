from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element_by_xpath("//*[@id='box6']")
target = driver.find_element_by_xpath("//*[@id='box106']")

action = ActionChains(driver)
action.drag_and_drop(source,target).perform()
