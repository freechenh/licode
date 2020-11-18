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

myself_button = '//li[@id="ttbar-myjd"]//a[contains(text(), "我的京东")]'

my_focus = '//dd[@id="_MYJD_product"]/a[contains(text(), "关注商品")]'

maotai = '//div[@id="goods_100012043978"]/div[@class="item-inner"]//a[contains(text(), "茅台")]'

num_add = "//a[@class='btn-add']"

add_cart = "//a[@id='InitCartUrl']"


class Jd:
    def __init__(self):
        url = "https://passport.jd.com/uc/login?ltype=logout"

        self.driver = webdriver.Chrome()
        # self.driver = webdriver.C
        self.driver.maximize_window()

        self.driver.get(url)

    def find_element_exist(self, ele_xpath):
        while True:
            try:
                ele = self.driver.find_element(By.XPATH, ele_xpath)
                return ele
            except NoSuchElementException:
                pass

    def query_maotai(self):
        find_text = self.find_element_exist(find_)
        find_text.send_keys("茅台")
        click_button = self.find_element_exist(search_button)
        click_button.click()

    def enter_myself(self):
        enter_ = self.find_element_exist(myself_button)
        enter_.click()
        self.switch_frame()

    def enter_my_focus(self):
        enter_ = self.find_element_exist(my_focus)
        enter_.click()

    def enter_goods_page(self):
        enter_ = self.find_element_exist(maotai)
        enter_.click()
        self.switch_frame()

    def switch_frame(self, n=-1):
        window = self.driver.window_handles
        self.driver.switch_to.window(window[n])

    def num_add_one(self):
        num = self.find_element_exist(num_add)
        num.click()

    def cart_add(self):
        cart = self.find_element_exist(add_cart)
        cart.click()

    def quit(self):
        self.driver.quit()


def main():
    demo = Jd()
    demo.enter_myself()
    time.sleep(2)
    # demo.switch_frame()
    time.sleep(2)
    demo.enter_my_focus()
    time.sleep(2)
    demo.enter_goods_page()
    time.sleep(10)
    # demo.switch_frame()
    time.sleep(10)
    demo.quit()


if __name__ == '__main__':
    main()
