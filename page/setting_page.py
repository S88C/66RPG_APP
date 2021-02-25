from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class SettingPage(BaseAction):
    # 退出登录
    logout_button = By.XPATH, "//*[@text='退出登录']"

    # 退出提示弹窗确认按钮
    logout_popup_ok = By.ID, "main.opalyer:id/pop_choose_right_txt"

    # 点击 退出登录
    @allure.step(title="设置 - 点击 退出登录")
    def click_logout(self):
        log.info("正在点击退出登录")
        self.find_element_with_scroll(self.logout_button).click()

    # 点击 退出提示弹窗的确认
    @allure.step(title="设置 - 点击 退出登录确认按钮")
    def click_logout_ok(self):
        log.info("正在点击确认按钮")
        self.click(self.logout_popup_ok)
