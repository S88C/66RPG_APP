import time

from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

# 获取日志入口
from base.get_logger import GetLogger

log = GetLogger().get_logger()


class MePage(BaseAction):
    # 我的 头像
    user_img = By.ID, "main.opalyer:id/home_self_xrv_header_face"
    # 设置 按钮
    setting_button = By.ID, "main.opalyer:id/home_self_xrv_header_setting"
    # 关于 按钮
    about_button = By.XPATH, "//*[@text='关于']"

    # 向下滑动屏幕
    @allure.step(title="我的 - 滑动 屏幕")
    def scroll_down_window(self):
        log.info("正在向下滑动屏幕")
        self.scroll_page_one_time("down")

    # 点击 头像
    @allure.step(title="我的页面 - 点击 头像")
    def click_user_img(self):
        log.info("正在点击头像")
        self.click(self.user_img)

    # 点击 设置
    @allure.step(title="我的 - 点击 设置")
    def click_setting(self):
        log.info("正在点击设置")
        self.click(self.setting_button)

    # 点击 关于
    @allure.step(title="设置 - 点击 关于")
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()
