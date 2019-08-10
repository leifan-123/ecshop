"""
购物车页面
"""

from common.base import Base


class CarPage(Base):
    """元素定位"""
    add_car_loc = ("id","com.tpshop.malls:id/add_cart_tv")  # 添加购物车
    goto_car_loc = ("id","com.tpshop.malls:id/bottom_cart_rl1") # 点击购物车
    ensure_loc = ("id","com.tpshop.malls:id/confirm_tv")    # 确定
    buygoods_loc = ("id","com.tpshop.malls:id/buy_tv")  # 立即购买
    backcar_loc = ("id","com.tpshop.malls:id/title_back_img") # 返回


    """元素操作"""
    def addcar_click(self):
        """添加购物车"""
        self.click(self.add_car_loc)

    def gocar_click(self):
        """点击购物车"""
        self.click(self.goto_car_loc)

    def click_ensure(self):
        """点击确定"""
        self.click(self.ensure_loc)

    def buygoods_click(self):
        """点击立即购买"""
        self.click(self.buygoods_loc)

    def back_car(self):
        """返回购物车"""
        # self.click(self.backcar_loc)
        x = 30
        y = 50
        self.coordinate(x=x,y=y)