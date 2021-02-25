from page.popup import PopupPage
from page.search_page import SearchPage
from page.works_page import WorksPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.about_page import AboutPage
from page.setting_page import SettingPage
from page.user_page import UserPage
from page.comment_page import CommentPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def popup(self):
        return PopupPage(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def works(self):
        return WorksPage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def about(self):
        return AboutPage(self.driver)

    @property
    def user(self):
        return UserPage(self.driver)

    @property
    def comment(self):
        return CommentPage(self.driver)
