import time

import allure
import pytest

from common.base import preposition_code,Base
from page.buy_page import BuySalesPage
from page.check_order_page import CheckOrderPage
from page.home_page import HomePage
from page.personal_page import PersonalPage
from page.car_page import CarPage


class TestBuyGoods:
    def setup_class(self):
        self.driver = preposition_code()


    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="使用余额购买商品")
    def test_buy_goods(self):
        allure.attach("点击我的", "进入个人中心")
        # 进入我的
        PersonalPage(self.driver).personal_click()
        # 获取金额
        money_b = float(PersonalPage(self.driver).get_value())
        allure.attach("购买商品前的金额:", f'{money_b}')
        allure.attach("点击首页", "进入商品促销")
        # 点击首页
        HomePage(self.driver).homepage_click()
        time.sleep(5)
        # 选择商品
        allure.attach("选择商品", "进入商品详情")
        HomePage(self.driver).goods_click()
        time.sleep(5)
        allure.attach("进入商品", "加入购物车")
        # 添加购物车
        CarPage(self.driver).addcar_click()
        # 确定
        CarPage(self.driver).click_ensure()
        allure.attach("选择商品", "进入购物车")
        # 点击购物车
        CarPage(self.driver).gocar_click()
        # 点击立即购买
        allure.attach("购物车", "立即购买")
        BuySalesPage(self.driver).buy_click()
        time.sleep(5)
        # 点击使用余额
        allure.attach("支付界面", "使用余额支付")
        CheckOrderPage(self.driver).balance_click()
        time.sleep(2)
        # 获取订单金额
        price = float(CheckOrderPage(self.driver).get_goods_price().strip("¥"))
        allure.attach("购买商品的金额:", f'{price}')
        # 点击提交订单
        CheckOrderPage(self.driver).submit_click()
        time.sleep(2)
        # 输入支付密码
        text = "123456"
        CheckOrderPage(self.driver).check_pwd_input(text)
        # 点击确定
        CheckOrderPage(self.driver).sure_click()
        time.sleep(2)
        # 点击返回上一页
        self.driver.back()
        # 进入个人中心
        PersonalPage(self.driver).personal_click()
        # 获取金额
        money_f = float(PersonalPage(self.driver).get_value())
        allure.attach("购买商品后的金额:", f'{money_f}')
        # 断言
        if money_b - price == money_f:
            assert 1
        else:
            Base(self.driver).screenshot("../screenshot/buy_sales.png")
            assert 0

    def teardown_class(self):
        """关闭app"""
        Base(self.driver).close()
