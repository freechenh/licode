import time

import requests
from selenium import webdriver

from day19.driver import Driver

url = "https://login.taobao.com/member/login.jhtml"

qrcode_path = '//div[@id="login"]/div[contains(@class, "view-type-qrcode")]/i'

J_SiteNavFavor = "//li[@id='J_SiteNavFavor']"

collections_dotey = "//a[contains(text(), '收藏的宝贝')]"


class TaoBao(Driver):

    def __init__(self, get_url):
        super().__init__(get_url)

    def click_qrcode(self):
        ele = self.find_ele_exit(qrcode_path)
        ele.click()

    def into_collections(self):
        pass


def main():
    demo = TaoBao(url)
    demo.click_qrcode()
    demo.quit()


if __name__ == '__main__':
    main()
