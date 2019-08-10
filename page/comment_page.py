"""
评价晒单
"""
from common.base import Base,preposition_code
import time

from page.order_show_page import OrderShowPage
from page.personal_page import PersonalPage


class CommentPage(Base):
    """元素定位"""
    content_loc = ("id","com.tpshop.malls:id/comment_content_et")   # 输入评价信息
    submitc_loc = ("xpath","//*[@text = '提交']")  # 提交
    star_loc = ("id","com.tpshop.malls:id/star5_btn")   # 星星等级

    """元素操作"""
    def inpute_content(self,text):
        """输入评价信息"""
        self.send_keys(self.content_loc,text)

    def submitc_click(self):
        """点击提交"""
        self.click(self.submitc_loc)

    def click_start(self):
        """查询星星"""
        starts = self.find_elements(self.star_loc)
        for start in starts:
            start.click()
            time.sleep(1)

if __name__ == '__main__':
    driver = preposition_code()
    PersonalPage(driver).personal_click()
    # 点击待评价
    PersonalPage(driver).comment_click()
    # 选择待评价的订单
    OrderShowPage(driver).order_click()
    # 输入评价
    text = "棒棒棒!!!!"
    CommentPage(driver).inpute_content(text)
    time.sleep(2)
    # 选择星星等级
    CommentPage(driver).click_start()
