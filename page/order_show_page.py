"""
晒单评价
"""
from common.base import Base, preposition_code
from page.personal_page import PersonalPage


class OrderShowPage(Base):
    """元素定位"""
    order_loc = ("xpath","//*[@text = '评价晒单']") # 待评价订单

    """元素操作"""
    def order_click(self):
        """点击晒单评价"""
        orders = self.find_elements(self.order_loc)
        orders[0].click()





if __name__ == '__main__':
    driver = preposition_code()
    # 进入我的
    PersonalPage(driver).personal_click()
    # 点击待评价
    PersonalPage(driver).comment_click()
    # 选择待评价的订单
    OrderShowPage(driver).order_click()