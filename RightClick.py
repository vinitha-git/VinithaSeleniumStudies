from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element_by_xpath("html/body/div/section/div/div/div/p/span")
action = ActionChains(driver)
action.context_click(button).perform()
