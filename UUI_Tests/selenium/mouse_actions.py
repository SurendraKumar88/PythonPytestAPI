import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://amazon.com")
driver.implicitly_wait(10)
driver.maximize_window()

sign_in = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
action = ActionChains(driver)

action.move_to_element(sign_in).perform()

driver.find_element(By.XPATH, "//span[text()='Create a List']").click()



time.sleep(10)