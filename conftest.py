import time
import pytest
from common.base import preposition_code
from page.login_page import LoginPage


@pytest.fixture()
def login():
    driver = preposition_code()
    LG = LoginPage(driver)
    LG.mine_click()
    time.sleep(2)
    LG.login_click()
    time.sleep(2)
    text = "18000180007"
    LG.input_username(text)
    time.sleep(2)
    pwd = "123456"
    LG.input_password(pwd)
    time.sleep(2)
    LG.loginto_click()
    time.sleep(5)


@pytest.fixture()
def random_test():
    print("测试随机数")
