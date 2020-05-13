from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver =webdriver.Chrome(executable_path="D:\Vinitha\sw\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
userElement = driver.find_element_by_name("userName")
print(userElement.is_displayed())
print(userElement.is_enabled())

passwordElement = driver.find_element_by_name("password")
print(passwordElement.is_displayed())
print(passwordElement.is_enabled())

userElement.send_keys("mercury")
passwordElement.send_keys("mercury")

driver.find_element_by_name("login").click()
roundTripElement = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button", roundTripElement.is_selected())

oneWayElement = driver.find_element_by_css_selector("input[value=oneway]")
print("status of one way radio Button", oneWayElement.is_selected())





