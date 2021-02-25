from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
from page.home_page import HomePage
import allure

# 获取日志入口


log = GetLogger().get_logger()


class SearchPage(BaseAction):

    # 搜索输入框
    search_input = By.ID, "main.opalyer:id/search_et"
    # 搜索按钮
    search_button = By.ID, "main.opalyer:id/search_do_search_tv"
    # 点击搜索页面第一个作品
    search_works = By.ID, "main.opalyer:id/search_ll"
    # 相关作者
    search_author = By.ID, "main.opalyer:id/author_tv"

    # 输入 搜索内容
    def __init__(self, driver):
        super().__init__(driver)
        self.home = HomePage(self.driver)

    @allure.step(title="搜索页 - 输入 搜索内容")
    def input_search(self, value):
        log.info("正在输入搜索内容")
        self.input(self.search_input, value)

    # 点击 搜索按钮
    @allure.step(title="home页 - 点击 开启新体验")
    def click_search_btn(self):
        log.info("正在点击搜索按钮")
        self.click(self.search_button)

    # 点击 作品
    @allure.step(title="搜索页 - 点击 作品")
    def click_works(self):
        log.info("正在点击作品")
        self.click(self.search_works)

    # 点击 相关用户
    @allure.step(title="搜索页 - 点击 相关用户")
    def click_author(self):
        log.info("正在点击相关用户")
        self.click(self.search_author)

    # 组合业务方法
    def page_search(self, name):
        self.home.click_searchbox()
        # 搜索页 - 输入 搜索内容
        self.input_search(name)
        # 搜索页 - 点击 搜索按钮
        self.click_search_btn()
        # 搜索页 - 点击 作品
        self.click_works()
