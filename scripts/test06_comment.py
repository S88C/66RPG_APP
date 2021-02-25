import time

from base.get_logger import GetLogger
from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
from page.search_page import SearchPage

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestComment:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.search = SearchPage(self.driver)
        # 等待广告
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("comment_data", "test_comment"))
    def test_comment(self, args):
        # 解析数据
        name = args["name"]
        value = args["value"]
        toast = args["toast"]
        log.info("当前name为:%s,value为:%s,toast为:%s" % (name, value, toast))
        # 调用搜索业务
        self.search.page_search(name)
        time.sleep(2)
        # 作品详情页 点击 评论按钮
        self.page.works.click_comment()
        # 评论页 点击 输入框
        self.page.comment.click_input_box()
        # 评论页 输入 文字
        self.page.comment.input_value(value)
        # 评论页 点击 发送
        self.page.comment.click_send()
        try:
            # 断言
            assert self.page.comment.is_toast_exist(toast)
        except:
            self.page.comment.click_send()
            assert self.page.comment.is_toast_exist("您发布的评论内容不恰当，请勿发布敏感或重复内容。")
