"""
基础方法
"""
import random
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time


def preposition_code(package="com.tpshop.malls", activity=".SPMainActivity", desi_name="android", version="5.1.1",
                     devicename="127.0.0.1:21503"):
    # 配置启动参数
    desired_caps = {}
    # 指定系统名称
    desired_caps["platformName"] = desi_name
    # 指定系统版本
    desired_caps["platformVersion"] = version
    # 指定设备名称
    desired_caps["deviceName"] = devicename
    # 指定app包名
    desired_caps["appPackage"] = package
    # 指定APP启动名
    desired_caps["appActivity"] = activity
    # 启动unicode输入法
    desired_caps["unicodeKeyboard"] = True
    # 重置键盘
    desired_caps["resetKeyboard"] = True
    # 不重置应用
    desired_caps["noReset"] = True
    # 添加一个新参数
    desired_caps["automationName"] = "Uiautomator2"
    # 打开手机(app)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver





class Base:
    def __init__(self, driver):
        """打开app"""
        self.driver = driver

    def close(self):
        """关闭app"""
        self.driver.close_app()

    def quit(self):
        """关闭驱动"""
        self.driver.quit()

    def find_element(self, locator, timeout=10):
        """定位单个元素"""
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        """定位多个元素"""
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator, timeout=10):
        """做元素点击"""
        element = self.find_element(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """输入"""
        element = self.find_element(locator, timeout)
        element.clear()  # 清空
        element.send_keys(text)  # 输入数据

    def screenshot(self, file_path):
        """截屏"""
        self.driver.get_screenshot_as_file(file_path)


    def coordinate(self, coor=None, x=None, y=None):
        """坐标点击"""
        TouchAction(self.driver).tap(element=coor, x=x, y=y).perform()

    def find_click(self,locator):
        """查找元素并点击"""
        try:
            self.find_element(locator).click()
        except:
            window = self.driver.get_window_size()
            x1 = window['width'] * 0.5
            y1 = window['height'] * 0.75
            y2 = window['height'] * 0.25
            self.driver.swipe(x1, y1, x1, y2, duration=5000)
            self.find_click(locator)


    def random_choice(self,locator):
        """随机选择"""
        elements = self.find_elements(locator)
        goods_list = []
        for ele in elements:
            goods_list.append(ele)
        index = random.randint(0,len(goods_list)-1)
        if goods_list[index]:
            goods_list[index].click()
        else:
            window = self.driver.get_window_size()
            x1 = window['width'] * 0.5
            y1 = window['height'] * 0.75
            y2 = window['height'] * 0.25
            self.driver.swipe(x1, y1, x1, y2, duration=5000)

    def refresh(self):
        self.driver.refresh()


    def get_text(self,locator):
        """获取文本"""
        element = self.find_element(locator)
        price = element.get_attribute("text")
        return price




if __name__ == '__main__':
    sales_loc = ("xpath","//*[@text = '商品促销']")  # 商品促销
    driver = preposition_code()
    time.sleep(3)
    B = Base(driver)
    time.sleep(5)
    B.click(sales_loc)


