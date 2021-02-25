from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class CommentPage(BaseAction):
    # 输入框
    input_box = By.ID, "main.opalyer:id/comment_self_txt"
    # 输入
    input_txt = By.ID, "main.opalyer:id/input_comm_pop_edit"
    # 发送按钮
    input_send = By.ID, "main.opalyer:id/input_comm_pop_txt_send"

    # 点击 输入框
    @allure.step(title="评论页 - 点击 输入框")
    def click_input_box(self):
        log.info("正在点击输入框")
        self.click(self.input_box)

    # 输入 文字
    @allure.step(title="评论页 - 输入 文字")
    def input_value(self, value):
        log.info("正在输入文字")
        self.input(self.input_txt, value)

    # 点击 发送按钮
    @allure.step(title="评论页 - 点击 发送按钮")
    def click_send(self):
        log.info("正在发送按钮")
        self.click(self.input_send)
