from page.home_page import HomePage
from page.login_page import Login_Page
from page.me import MePage
from page.register_page import Register_Page


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def register(self):
        return Register_Page(self.driver)

    @property
    def login(self):
        return Login_Page(self.driver)

    @property
    def me(self):
        return MePage(self.driver)