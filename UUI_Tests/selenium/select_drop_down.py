import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://facebook.com")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").click()

birth_day = driver.find_element(By.NAME, "birthday_day")
birth_month = driver.find_element(By.NAME, "birthday_month")
birth_year = driver.find_element(By.NAME, "birthday_year")

select_day = Select(birth_day)
select_day.select_by_visible_text("7")

select_day = Select(birth_month)
select_day.select_by_visible_text("Nov")

select_day = Select(birth_year)
select_day.select_by_visible_text("1993")
time.sleep(10)