import allure
import pytest
from common.base import preposition_code,Base
from page.comment_page import CommentPage
from page.personal_page import PersonalPage
from page.order_show_page import OrderShowPage
import time


class TestGoodsComment:
    def setup_class(self):
       self.driver = preposition_code()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="评论")
    def test_goods_comment(self):
        """商品评论"""
        allure.attach("点击我的", "进入个人中心")
        # 进入我的
        PersonalPage(self.driver).personal_click()
        time.sleep(1)
        # 选择待评价
        PersonalPage(self.driver).comment_click()
        # 选择待评价的订单
        allure.attach("进入待评价", "选择待评价订单")
        OrderShowPage(self.driver).order_click()
        # 输入评价
        text = "陌上花开,缓缓归矣!"
        CommentPage(self.driver).inpute_content(text)
        time.sleep(2)
        # 选择星星等级
        CommentPage(self.driver).click_start()
        # 点击提交
        CommentPage(self.driver).submitc_click()
        time.sleep(1)
        allure.attach("评论成功", "获取toast")
        # 获取toast文本
        toast = self.driver.find_element_by_xpath("//*[contains(@text,'成功')]")
        text = toast.text
        # 断言
        if text == "评论成功":
            assert 1
        else:
            Base(self.driver).screenshot("../screenshot/comment.png")
            assert 0


    def teardown_class(self):
        """关闭app"""
        Base(self.driver).close()