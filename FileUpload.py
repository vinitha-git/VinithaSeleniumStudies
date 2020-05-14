from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("D:\Vinitha\sw\\download (1).jpg")

