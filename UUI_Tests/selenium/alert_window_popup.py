import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

driver.maximize_window()
time.sleep(5)

button = driver.find_element(By.XPATH, "//button[text()='Button']")
time.sleep(2)
driver.execute_script("window.scrollBy(0,300)","")
#driver.execute_script("arguments[0].scrollIntoView();",button)

time.sleep(5)
button.click()
time.sleep(5)

alt = driver.switch_to.alert
alt.accept()

windows = driver.window_handles
print(windows)

driver.switch_to.window(windows[1])
print("currently in child window")
time.sleep(5)
driver.switch_to.window(windows[0])
print("currently in parent window")

time.sleep(10)