import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=30.0, poll=1.0):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一个元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
        # return self.driver.find_element(*feature)

    def find_elements(self, feature, timeout=30.0, poll=1.0):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一组元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature, timeout=30.0, poll=1.0):
        """
        根据特征，点击元素
        :param feature: 特征
        :return:
        """
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, value, timeout=30.0, poll=1.0):
        """
        根据特征，先清空，再输入文字
        :param feature: 特征
        :param value: 文字
        :return:
        """
        self.clear(feature, timeout, poll)
        self.find_element(feature, timeout, poll).send_keys(value)

    def clear(self, feature, timeout=30.0, poll=1.0):
        """
        根据特征，清空
        :param feature: 特征
        :return:
        """
        self.find_element(feature, timeout, poll).clear()

    def get_feature_text(self, feature, timeout=30.0, poll=1.0):
        """
        根据元素的特征，获取元素的文字内容
        :param feature: 元素的特征
        :return: 元素的文字内容
        """
        if self.is_feature_exist(feature, timeout, poll):
            return self.find_element(feature, timeout, poll).text
        else:
            raise Exception("没有找到，对应的feature的元素，请检查。")

    def is_feature_exist(self, feature, timeout=30.0, poll=1.0):
        """
        根据元素的特征，判断这个元素是否存在
        :param feature: 元素的特征
        :return: 是否存在
        """
        try:
            self.find_element(feature, timeout, poll)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message, timeout=10.0, poll=0.1):
        """
        根据toast的部分消息，获取全部的toast的文字内容
        :param message: 部分消息
        :return: 全部的toast的文字内容
        """
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        if self.is_feature_exist(toast_feature, timeout, poll):
            return self.find_element(toast_feature, timeout, poll).text
        else:
            raise Exception("没有找到，对应的toast内容，请检查。")

    def is_toast_exist(self, message, timeout=10.0, poll=0.1):
        """
        根据toast的部分消息，判断toast是否存在
        :param message: 部分消息
        :return: 是否存在
        """
        toast_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        return self.is_feature_exist(toast_feature, timeout, poll)

    def scroll_page_one_time(self, direction="up"):
        """
        滑动一次屏幕
        :param dir: 滑动的方向
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return:
        """
        # 滑动
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        top_x = screen_width * 0.5
        top_y = screen_height * 0.25
        bottom_x = screen_width * 0.5
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = screen_height * 0.5
        right_x = screen_width * 0.75
        right_y = screen_height * 0.5

        # 根据方向参数，去滑动
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请输入正确的滑动方向 up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        """
        按照 dir 的方向滑动，并且找到 feature 这个特征的元素
        :param dir:
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return: 找到的元素
        """
        while True:
            try:
                # 如果找到元素，就点进去
                # driver.find_element_by_xpath("//*[@text='用户']").click()
                # return self.driver.find_element(*feature)
                return self.find_element(feature)
            except TimeoutException:

                # 记录一下滑动之前的page_source
                old_page_source = self.driver.page_source

                self.scroll_page_one_time(direction)

                # 判断滑动之后是不是和之前的页面一样
                if old_page_source == self.driver.page_source:
                    raise Exception("到底了！请检查传入的元素的特征")

    def is_keyword_in_page_source(self, keyword, timeout=5.0, poll=0.5):
        """
        判断 keyword 是否在当前页面的 page_source 中
        :param keyword: 需要查询的字符串
        :return: 是否在页面中
        """
        end_time = time.time() + timeout
        while True:
            res = keyword in self.driver.page_source
            if res:
                return True

            if time.time() > end_time:
                return False

            time.sleep(poll)
