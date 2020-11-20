# import requests
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class Driver:

    def __init__(self, url=None):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def quit(self):
        sleep(10)
        self.driver.quit()

    def find_ele_exit(self, ele_path=None):
        """确定元素存在"""
        while True:
            try:
                ele = self.driver.find_element(By.XPATH, ele_path)
                return ele
            except NoSuchElementException:
                pass

    def suspension(self, ele_path=None):
        """悬浮并点击"""
        ac = ActionChains(self.driver)
        ele = self.find_ele_exit(ele_path)
        ac.move_to_element(ele).perform()
        sleep(1)
        ac.click(ele).perform()
