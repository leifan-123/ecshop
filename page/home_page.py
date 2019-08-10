"""
首页
"""
from common.base import Base,preposition_code
import time

class HomePage(Base):
    """定位元素"""
    homepage_loc = ("id","com.tpshop.malls:id/home_tv") # 首页
    sales_loc = ("xpath","//*[@text = '商品促销']") # 商品促销
    goods_loc = ("xpath","//*[@text = '航测试手机']")    # 无促销商品

    """元素操作"""
    def homepage_click(self):
        """点击首页"""
        self.click(self.homepage_loc)

    def sales_click(self):
        """点击商品促销"""
        self.click(self.sales_loc)

    def goods_click(self):
        """无促销商品点击"""
        self.find_click(self.goods_loc)

if __name__ == '__main__':
    driver = preposition_code()
    # LG = LoginPage(driver)
    # time.sleep(2)
    # LG.mine_click()
    # time.sleep(2)
    # LG.login_click()
    # time.sleep(2)
    # text = "18000180006"
    # LG.input_username(text)
    # time.sleep(2)
    # pwd = "123456"
    # LG.input_password(pwd)
    # time.sleep(2)
    # LG.loginto_click()
    # time.sleep(2)
    HP = HomePage(driver)
    HP.homepage_click()
    # time.sleep(2)
    # HP.sales_click()
    # time.sleep(2)
    HP.goods_click()
    time.sleep(2)
