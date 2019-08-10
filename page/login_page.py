"""
登录/注册界面
"""
from common.base import Base,preposition_code
import time


class LoginPage(Base):
    """定位元素"""
    mine_loc = ("id","com.tpshop.malls:id/mine_tv")    # 我的
    login_loc = ("id","com.tpshop.malls:id/head_img")    # 登录/注册
    username_loc = ("id","com.tpshop.malls:id/mobile_et")   # 账号
    password_loc = ("id","com.tpshop.malls:id/pwd_et")  # 密码
    loginto_loc = ("id","com.tpshop.malls:id/login_tv") # 登录

    """元素操作"""
    def mine_click(self):
        """点击我的"""
        self.click(self.mine_loc)

    def login_click(self):
        """点击登录/注册"""
        self.click(self.login_loc)

    def input_username(self,text):
        """输入账户"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)

    def loginto_click(self):
        """点击登录"""
        self.click(self.loginto_loc)


if __name__ == '__main__':
    driver = preposition_code()
    LG = LoginPage(driver)
    time.sleep(5)
    LG.mine_click()
    time.sleep(5)
    LG.login_click()
    time.sleep(5)
    text="18000180006"
    LG.input_username(text)
    time.sleep(5)
    pwd = "123456"
    LG.input_password(pwd)
    time.sleep(5)
    LG.loginto_click()






