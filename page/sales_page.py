"""
商品促销页面
"""
from common.base import Base,preposition_code
from page.home_page import HomePage
import time


class SalesPage(Base):
    """定位元素"""
    sales_goods_loc = ("class name","android.widget.ImageView")    # 促销商品

    """操作元素"""
    def sales_goods_click(self):
        """点击商品"""
        self.random_choice(self.sales_goods_loc)



if __name__ == '__main__':
    driver = preposition_code()
    SP = SalesPage(driver)
    HP = HomePage(driver)
    HP.sales_click()
    time.sleep(3)
    SP.sales_goods_click()