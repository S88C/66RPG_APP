from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class PopupPage(BaseAction):
    # 权限同意按钮
    power_ok = By.ID, "main.opalyer:id/pop_choose_right_txt"

    # 权限不同意按钮
    power_on = By.ID, "main.opalyer:id/pop_choose_left_txt"

    # 点击弹窗的同意
    @allure.step(title="启动页面 - 点击 同意")
    def click_popup_ok(self):
        log.info("正在点击'同意'按钮")
        self.click(self.power_ok)

    # 点击弹窗的不同意
    @allure.step(title="启动页面 - 点击 不同意")
    def click_popup_on(self):
        log.info("正在点击'不同意'按钮")
        self.click(self.power_on)
