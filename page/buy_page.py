"""
购买商品
"""
from common.base import Base


class BuySalesPage(Base):
    """元素定位"""
    buy_loc = ("xpath","//*[@text = '立即购买']")   # 立即购买
    ensure_loc = ("xpath","//*[@text = '确定']")   # 确定按钮

    """元素操作"""
    def buy_click(self):
        """点击立即购买"""
        self.click(self.buy_loc)

    def ensure_click(self):
        """点击确认"""
        self.click(self.ensure_loc)