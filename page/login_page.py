from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class LoginPage(BaseAction):
    # 点击密码登录
    login_pwdlogin = By.ID, "main.opalyer:id/layout_loginTitle_password"
    # 账号
    username_edit_text = By.ID, "main.opalyer:id/editText_pwLogin_user"
    # 密码
    password_edit_text = By.ID, "main.opalyer:id/editText_pwLogin_password"
    # 复选框
    login_checkbox = By.ID, "main.opalyer:id/checkBox_agree_pw"
    # 登录按钮
    login_button = By.ID, "main.opalyer:id/button_pwLogin"

    # 点击账号密码登录
    @allure.step(title="登录页面 - 点击 账号密码登录")
    def click_pwdlogin(self):
        log.info("正在点击账号密码登录按钮")
        self.click(self.login_pwdlogin)

    # 输入 账号
    @allure.step(title="登录页面 - 输入 账号")
    def input_username(self, value):
        log.info("正在输入账号:%s" % value)
        self.input(self.username_edit_text, value)

    # 输入 密码
    @allure.step(title="登录页面 - 输入 密码")
    def input_password(self, value):
        log.info("正在输入密码:%s" % value)
        self.input(self.password_edit_text, value)

    # 点击复选框
    @allure.step(title="登录页面 - 点击 复选框")
    def click_checkbox(self):
        log.info("正在点击复选框")
        self.click(self.login_checkbox)

    # 点击登录按钮
    @allure.step(title="登录页面 - 点击 登录")
    def click_loginbtn(self):
        log.info("正在点击登录按钮")
        self.click(self.login_button)
