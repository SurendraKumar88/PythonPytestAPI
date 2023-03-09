from UUI_Tests.Config.config import TestData
from UUI_Tests.Pages.LoginPage import LoginPage
from UUI_Tests.Tests.test_base import BaseTest


class TestLogin(BaseTest):
    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title_of_the_page()
        assert title == TestData.LOGIN_PAGE_TITLE


    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_app(TestData.USER_NAME, TestData.PASSWORD)
