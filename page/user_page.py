from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class UserPage(BaseAction):
    # 用户名
    user_name = By.ID, "main.opalyer:id/tv_friendly_gname"
    # 关注按钮
    follow_button = By.ID, "main.opalyer:id/friendly_pay_attention_layout"

    # 输入 搜索内容
    @allure.step(title="个人详情页 - 获取 用户名")
    def get_username(self):
        log.info("正在获取用户名")
        return self.get_feature_text(self.user_name)

    # 点击/取消 关注
    @allure.step(title="个人详情页 - 点击 关注/取消")
    def click_follow(self):
        log.info("正在点击关注/取消按钮")
        return self.click(self.follow_button)
