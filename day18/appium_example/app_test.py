import os

import pytest
from appium import webdriver

from time import sleep


# = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


# def file_path(p):
#     return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


@pytest.fixture()
def web_set_up():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = "io.appium.android.apis"
    desired_caps['appActivity'] = "io.appium.android.apis.ApiDemos"
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver


@pytest.fixture()
def web_tear_down():
    yield


class TestApp:

    def test_open_app(self, web_set_up):
        pass
