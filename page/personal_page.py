"""
我的
"""
from common.base import Base



class PersonalPage(Base):
    """元素定位"""
    personal_loc = ("xpath","//*[@text = '我的']")
    receive_loc = ("id","com.tpshop.malls:id/wait_receive_ll")  # 待收货
    comment_loc = ("id","com.tpshop.malls:id/wait_comment_ll")  # 待评论
    money_loc = ("id","com.tpshop.malls:id/balance_tv")

    """元素操作"""
    def personal_click(self):
        """点击我的"""
        self.click(self.personal_loc)

    def receive_click(self):
        """点击待收货"""
        self.click(self.receive_loc)

    def comment_click(self):
        """点击待评价"""
        self.click(self.comment_loc)

    def get_value(self):
        """获取金额"""
        return self.get_text(self.money_loc)