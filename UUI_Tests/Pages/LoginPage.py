from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//div[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.APP_URL)

    def get_title_of_the_page(self):
        return self.get_title()

    def login_app(self, user_name, password):
        self.send_keys(self.USER_NAME, user_name)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
