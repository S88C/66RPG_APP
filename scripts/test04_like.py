import time

from base.get_logger import GetLogger
from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
from page.search_page import SearchPage

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestLike:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.search = SearchPage(self.driver)
        # 等待广告
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("search_data", "test_search_name"))
    def test_like(self, args):
        name = args["name"]
        # 调用搜索方法
        self.search.page_search(name)
        time.sleep(2)
        # 作品详情页 查找 点赞按钮
        self.page.works.scroll_lick()
        # 作品详情页 判断 点赞状态是不是为未点赞
        if not self.page.works.get_like_state() == "已点赞":
            # 作品详情页 点击 点赞按钮
            self.page.works.click_like()
            # 作品详情页 断言 点赞状态
            assert self.page.works.get_like_state() == "已点赞"

