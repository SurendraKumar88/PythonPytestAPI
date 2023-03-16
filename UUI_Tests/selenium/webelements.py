import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://google.com")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Gmail']").click()
time.sleep(10)