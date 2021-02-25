import time

from base.get_logger import GetLogger
from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
from page.search_page import SearchPage

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestCollect:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.search = SearchPage(self.driver)
        # 等待广告
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("search_data", "test_search_name"))
    def test_collect(self, args):
        name = args["name"]
        self.search.page_search(name)
        time.sleep(2)
        # 作品详情页 查找 收藏按钮
        self.page.works.scroll_lick()
        # 作品详情页 判断 收藏状态
        if self.page.works.get_collect_state() == "收藏":
            # 作品详情页 点击 收藏按钮
            self.page.works.click_collect()
            # 作品详情页 点击 精选集复选框
            self.page.works.click_collect_checkbox()
            # 作品详情页 点击 确认按钮
            self.page.works.click_collect_ok()
            # 作品详情页 判断 toast
            if self.page.works.is_toast_exist("收藏成功"):
                # 作品详情页 断言 收藏状态
                assert self.page.works.get_collect_state() == "已收藏"
            else:
                assert False
        else:
            # 作品详情页 点击 收藏按钮
            self.page.works.click_collect()
            # 作品详情页 点击 精选集复选框
            self.page.works.click_collect_checkbox()
            # 作品详情页 点击 确认按钮
            self.page.works.click_collect_ok()
            # 作品详情页 判断 toast
            if self.page.works.is_toast_exist("取消收藏成功"):
                # 作品详情页 断言 收藏状态
                assert self.page.works.get_collect_state() == "收藏"
            else:
                assert False
