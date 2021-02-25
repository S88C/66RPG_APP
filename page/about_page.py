from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class AboutPage(BaseAction):
    # 检查更新
    update_button = By.XPATH, "//*[@text='检查更新']"
    # 版本更新状态
    update_txt = By.ID, "main.opalyer:id/about_item_common_update"

    # 点击 检查更新
    @allure.step(title="关于 - 点击 检查更新")
    def click_update_btn(self):
        log.info("正在点击检查更新")
        self.find_element_with_scroll(self.update_button).click()

    # 获取 更新状态
    @allure.step(title="关于 - 获取 更新状态")
    def get_update_txt(self):
        log.info("正在获取更新状态")
        return self.get_feature_text(self.update_txt)

