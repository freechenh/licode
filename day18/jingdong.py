#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: jingdong.py
# @Author: dell
# @Date: 2020/11/17  18:48
# @Desc: 
# @Project: licode
# @Source: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver.common.utils import
# from

find_ = "//input[@id='key']"

search_button = "//button[@class='button']"


class Jd:
    def __init__(self):
        url = "https://passport.jd.com/uc/login?ltype=logout"

        self.driver = webdriver.Chrome()
        # self.driver = webdriver.C
        self.driver.maximize_window()

        self.driver.get(url)

    def query_maotai(self):
        while True:
            try:
                find_text = self.driver.find_element(By.XPATH, find_)
                find_text.send_keys("茅台")
                click_button = self.driver.find_element(By.XPATH, search_button)
                click_button.click()
                break
            except NoSuchElementException:
                pass

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    demo = Jd()
    demo.query_maotai()
    demo.quit()
