import time

from base.get_logger import GetLogger
from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestLogin:

    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)
        log.info("正在初始化Driver")
        # 首页 - 点击 弹窗的同意
        self.page.popup.click_popup_ok()
        print("正在开始测试")
        # 等待广告
        time.sleep(5)
        # 点击开启新体验
        self.page.home.click_update_popup()
        # 主页 - 点击 我的
        self.page.home.click_my()
        time.sleep(2)
        # 我的 - 滑动 屏幕
        self.page.me.scroll_down_window()
        # 我的 - 判断登录状态
        if not self.page.login.is_toast_exist("未登录"):
            # 我的 - 点击 设置
            self.page.me.click_setting()
            # 设置 - 点击 退出登录
            time.sleep(1)
            self.page.setting.click_logout()
            # 设置 - 点击 弹窗确定
            self.page.setting.click_logout_ok()
            # 等待退出登录
            time.sleep(5)
            # 我的 - 滑动 屏幕
            self.page.me.scroll_down_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        # 获取数据
        print("正在获取数据")
        log.info("正在获取数据")
        username = args["username"]
        log.info("当前用户名为:%s" % username)
        password = args["password"]
        log.info("当前密码为:%s" % password)
        toast = args["toast"]
        log.info("当前Toast为:%s" % toast)

        # 我的 - 点击 头像
        self.page.me.click_user_img()
        # 登录 - 点击 账号密码登录
        self.page.login.click_pwdlogin()
        # 登录 - 输入 账号
        self.page.login.input_username(username)
        # 登录 - 输入 密码
        self.page.login.input_password(password)
        # 登录 - 点击 复选框
        self.page.login.click_checkbox()
        # 登录 - 点击 登陆
        self.page.login.click_loginbtn()
        print("开始断言")
        assert self.page.login.is_toast_exist(toast)
