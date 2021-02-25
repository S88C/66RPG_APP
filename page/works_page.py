from selenium.webdriver.common.by import By
from base.get_logger import GetLogger
from base.base_action import BaseAction
import allure

# 获取日志入口
log = GetLogger().get_logger()


class WorksPage(BaseAction):
    # 作品名称
    works_name = By.ID, "main.opalyer:id/fragment_details_item_gamemessage_txt_gname"
    # 搜索按钮
    works_author = By.ID, "main.opalyer:id/fragment_details_item_gamemessage_txt_aname"
    # 点击搜索页面第一个作品
    search_works = By.ID, "main.opalyer:id/search_ll"
    # 评论按钮
    comment_button = By.ID, "main.opalyer:id/detail_rl_title_2"
    # 点赞状态
    like_txt = By.ID, "main.opalyer:id/fragment_details_item_mine_txt_prise"
    # 点赞按钮
    like_button = By.ID, "main.opalyer:id/fragment_details_item_mine_img_prise"
    # 送花按钮
    flower_button = By.ID, "main.opalyer:id/fragment_details_item_mine_img_flower"
    # 收藏状态
    collect_txt = By.ID, "main.opalyer:id/fragment_details_item_mine_txt_collect"
    # 收藏按钮
    collect_button = By.ID, "main.opalyer:id/fragment_details_item_mine_ll_collect"
    # 收藏到
    collect_checkbox = By.ID, "main.opalyer:id/pop_copy_move_content_item_check_img"
    # 精选集确认按钮
    collect_ok = By.ID, "main.opalyer:id/pop_copy_move_sure_txt"

    # 获取 作品名
    @allure.step(title="搜索页 - 获取 作品名称")
    def get_works_name(self):
        log.info("正在获取作品名称")
        return self.get_feature_text(self.works_name)

    # 获取 作者名
    @allure.step(title="搜索页 - 获取 作者名称")
    def get_author_name(self):
        log.info("正在获取作者名称")
        return self.get_feature_text(self.works_author)

    # 点击 作品
    @allure.step(title="搜索页 - 点击 作品")
    def click_works(self):
        log.info("正在点击作品")
        self.click(self.search_works)

    # 点击 评论
    @allure.step(title="作品详情页 - 点击 评论")
    def click_comment(self):
        log.info("正在点击评论")
        self.click(self.comment_button)

    # 跳转 详细信息
    @allure.step(title="作品详情页 - 跳转 详细信息")
    def scroll_lick(self):
        log.info("正在跳转详细信息")
        self.find_element_with_scroll(self.flower_button)

    # 获取 点赞状态
    @allure.step(title="作品详情页 - 获取 点赞状态")
    def get_like_state(self):
        log.info("正在获点赞状态")
        return self.get_feature_text(self.like_txt)

    # 点击 点赞
    @allure.step(title="作品详情页 - 点击 点赞")
    def click_like(self):
        log.info("正在点击点赞")
        self.click(self.like_button)

    # 获取 收藏状态
    @allure.step(title="作品详情页 - 获取 收藏状态")
    def get_collect_state(self):
        log.info("正在获收藏状态")
        return self.get_feature_text(self.collect_txt)

    # 点击 收藏
    @allure.step(title="作品详情页 - 点击 收藏")
    def click_collect(self):
        log.info("正在点击收藏")
        self.click(self.collect_button)

    # 点击 精选集复选框
    @allure.step(title="作品详情页 - 点击 精选集复选框")
    def click_collect_checkbox(self):
        log.info("正在点击精选集复选框")
        self.click(self.collect_checkbox)

    # 点击 确认
    @allure.step(title="作品详情页 - 点击 确认")
    def click_collect_ok(self):
        log.info("正在点击确认")
        self.click(self.collect_ok)
