from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='textbox']").send_keys("Testing download files")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click()
