import time


from base.get_logger import GetLogger
from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestSearch:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        # 等待广告
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("search_data", "test_search_name"))
    def test_search_name(self, args):
        # 解析数据
        name = args["name"]
        author = args["author"]
        log.info("当前预期作品名为:%s,当前预期作者为:%s" % (name, author))
        # 调用搜索测试方法
        self.page.search.page_search(name)
        # 作品详情页 - 断言 作品名称与预期是否相符
        log.info("当前作品名为:%s,预期作品名为:%s" % (self.page.works.get_works_name(), name))
        assert name in self.page.works.get_works_name()
        log.info("断言通过")
        # 作品详情页 - 断言 作者名称与预期是否相符
        log.info("当前作者名为:%s,预期作者名为:%s" % (self.page.works.get_author_name(), author))
        assert author in self.page.works.get_author_name()
        log.info("断言通过")

    @pytest.mark.parametrize("args", analyze_data("search_data", "test_search_author"))
    def test_search_author(self, args):
        # 解析数据
        author = args["author"]
        log.info("当前预期作者为:%s" % author)
        # 主页 - 点击 搜索按钮
        self.page.home.click_searchbox()
        # 搜索页 - 输入 搜索内容
        self.page.search.input_search(author)
        # 搜索页 - 点击 搜索按钮
        self.page.search.click_search_btn()
        # 搜索页 - 点击 相关用户
        self.page.search.click_author()
        # 个人详情页 - 获取 用户名
        log.info("当前用户名为:% s,预期用户名为:%s" % (self.page.user.get_username(), author))
        assert author in self.page.user.get_username()
