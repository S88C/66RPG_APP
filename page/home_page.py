import time
import allure
from base.get_logger import GetLogger
from selenium.webdriver.common.by import By

from base.base_action import BaseAction
# 获取日志入口
log = GetLogger().get_logger()


class HomePage(BaseAction):
    # 升级弹窗
    update_popup = By.ID, "main.opalyer:id/updatebybrowser"
    # 搜索框
    search_box = By.ID, "main.opalyer:id/search_layout"
    # 我的
    me_button = By.ID, "main.opalyer:id/main_self_ll"

    # 点击 开启新体验按钮
    @allure.step(title="home页 - 点击 开启新体验")
    def click_update_popup(self):
        log.info("正在点击开启新体验按钮")
        self.click(self.update_popup)

    # 点击 我的
    @allure.step(title="home页 - 点击 我的")
    def click_my(self):
        log.info("正在点击我的按钮")
        self.click(self.me_button)

    # 点击 搜索框
    @allure.step(title="home页 - 点击 搜索框")
    def click_searchbox(self):
        log.info("正在点击搜索框")
        self.click(self.search_box)
