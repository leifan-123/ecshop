import time
class Swipe:
    def __init__(self, driver):
        self.driver = driver
        size = driver.get_window_size()
        self._width = size["width"]
        self._height = size["height"]

    def swipe_up(self):
        """向上滑动"""
        start_x = self._width * 0.5
        start_y = self._height * 0.75
        end_x = self._width * 0.5
        end_y = self._height * 0.25
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=5000)


    def swipe_down(self):
        """向下滑动"""
        start_x = self._width * 0.5
        start_y = self._height * 0.25
        end_x = self._width * 0.5
        end_y = self._height * 0.75
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=5000)

    def swipe_left(self,n=1):
        """向左滑动"""
        start_x = self._width * 0.75
        start_y = self._height * 0.5
        end_x = self._width * 0.25
        end_y = self._height * 0.5
        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=5000)
            time.sleep(2)

    def swipe_right(self,n=1):
        """向右滑动"""
        start_x = self._width * 0.25
        start_y = self._height * 0.5
        end_x = self._width * 0.75
        end_y = self._height * 0.5

        for i in range(n):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=5000)
            time.sleep(2)