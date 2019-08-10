import time

import allure
import pytest
from common.base import preposition_code,Base
from page.home_page import HomePage
from page.sales_page import SalesPage
from page.buy_page import BuySalesPage
from page.check_order_page import CheckOrderPage
from page.personal_page import PersonalPage


class TestBuySales:
    def setup_class(self):
        self.driver = preposition_code()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="使用余额购买促销商品")
    def test_buy_sales(self):
        allure.attach("点击我的","进入个人中心")
        PersonalPage(self.driver).personal_click()
        # 获取金额
        money_b = float(PersonalPage(self.driver).get_value())
        allure.attach("购买商品前的金额:",f'{money_b}')
        allure.attach("点击首页", "进入商品促销")
        # 进入首页
        HomePage(self.driver).homepage_click()
        time.sleep(2)
        # 点击促销商品
        HomePage(self.driver).sales_click()
        time.sleep(5)
        allure.attach("任意选择一商品", "进入商品详情")
        # 选择促销商品
        SalesPage(self.driver).sales_goods_click()
        time.sleep(5)
        allure.attach("商品详情","立即购买")
        # 点击立即购买
        BuySalesPage(self.driver).buy_click()
        time.sleep(5)
        # 点击确认
        BuySalesPage(self.driver).ensure_click()
        allure.attach("支付界面","使用余额支付")
        # 点击使用余额
        CheckOrderPage(self.driver).balance_click()
        time.sleep(3)
        # 获取订单金额
        price = float(CheckOrderPage(self.driver).get_goods_price().strip("¥"))
        allure.attach("购买商品的金额:", f'{price}')
        try:
            # self.driver.find_element_by_xpath("//*[contains(@text,'每人限购')]"):
            toast = self.driver.find_element_by_xpath("//*[contains(@text,'每人限购')]")
            print(toast.text)
        except:
            # 点击提交订单
            CheckOrderPage(self.driver).submit_click()
            time.sleep(3)
            allure.attach("提交订单", "输入支付密码")
            # 输入支付密码
            text = "123456"
            CheckOrderPage(self.driver).check_pwd_input(text)
            # 点击确定
            CheckOrderPage(self.driver).sure_click()
            # 点击返回上一页
            for i in range(4):
                self.driver.back()
                time.sleep(2)
            allure.attach("点击我的", "进入个人中心")
            # 进入个人中心
            PersonalPage(self.driver).personal_click()
            # 获取金额
            money_f = float(PersonalPage(self.driver).get_value())
            allure.attach("购买商品后的金额:", f'{money_f}')
            # 断言
            if money_b-price == money_f:
                assert 1
            else:
                Base(self.driver).screenshot("../screenshot/buy_sales.png")
                assert 0


    def teardown_class(self):
        """关闭app"""
        Base(self.driver).close()
