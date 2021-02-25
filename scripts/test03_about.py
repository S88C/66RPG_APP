import time


from base.get_logger import GetLogger
from base.base_driver import init_driver
from page.page import Page

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestAbout:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        # 等待广告
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    def test_about(self):
        # home - 点击 我的
        self.page.home.click_my()
        # 我的页面 - 点击 关于
        self.page.me.click_about()
        # 关于页面 - 点击 检查更新
        self.page.about.click_update_btn()
        # 关于页面 - 判断 更新状态
        assert "已经是最新版本" == self.page.about.get_update_txt()
        log.info("更新状态断言成功")
