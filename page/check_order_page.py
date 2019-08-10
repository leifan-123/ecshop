"""
促销商品确认订单
"""
import time
from common.base import Base, preposition_code
from page.buy_page import BuySalesPage
from page.home_page import HomePage
from page.sales_page import SalesPage


class CheckOrderPage(Base):
    """元素定位"""
    integral_loc = ("id", "com.tpshop.malls:id/order_point_sth")  # 积分
    balance_loc = ("id", "com.tpshop.malls:id/order_balance_sth")  # 余额
    submit_loc = ("id", "com.tpshop.malls:id/submit_tv")  # 提交订单
    input_pwd_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 支付密码
    sure_loc = ("id", "com.tpshop.malls:id/sure_tv")  # 确认
    goods_price_loc = ("id", "com.tpshop.malls:id/balance_fee_tv")  # 余额支付金额


    """元素操作"""

    def integral_click(self):
        """点击积分"""
        self.click(self.integral_loc)

    def balance_click(self):
        """点击余额"""
        self.click(self.balance_loc)

    def submit_click(self):
        """点击提交订单"""
        self.click(self.submit_loc)

    def check_pwd_input(self, text):
        """输入支付密码"""
        self.send_keys(self.input_pwd_loc, text)

    def sure_click(self):
        """点击确认"""
        self.click(self.sure_loc)

    def backhome_click(self):
        """返回首页"""
        self.click(self.backhome_click())

    def get_goods_price(self):
        """获取金额"""
        return self.get_text(self.goods_price_loc)


if __name__ == '__main__':
    driver = preposition_code()
    # 点击促销商品
    HomePage(driver).sales_click()
    time.sleep(5)
    # 选择促销商品
    SalesPage(driver).sales_goods_click()
    time.sleep(2)
    # 点击立即购买
    BuySalesPage(driver).buy_click()
    time.sleep(2)
    # 点击确认
    BuySalesPage(driver).ensure_click()
    # 点击使用积分
    CheckOrderPage(driver).integral_click()
    # 点击使用余额
    CheckOrderPage(driver).balance_click()
    # 点击提交订单
    CheckOrderPage(driver).submit_click()
    price = CheckOrderPage(driver).get_goods_price()
    print(price)
    time.sleep(3)
    # driver.switch_to_alert()
    # 输入支付密码
    text = "123456"
    CheckOrderPage(driver).check_pwd_input(text)
    time.sleep(3)
    # 点击确定
    CheckOrderPage(driver).sure_click()
    time.sleep(3)
    # 点击返回
    CheckOrderPage(driver).backhome_click()

