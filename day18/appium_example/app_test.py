import os

import pytest
from appium import webdriver

from time import sleep

# = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


# def file_path(p):
#     return os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",
    "appPackage": "io.appium.android.apis",
    "appActivity": "io.appium.android.apis.ApiDemos",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}


@pytest.fixture()
def web_set_up():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver


@pytest.fixture()
def idle_fish_set_up():
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['appPackage'] = "com.taobao.idlefish"
    desired_caps['appActivity'] = "com.taobao.fleamarket.home.activity.MainActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver


@pytest.fixture()
def web_tear_down():
    yield


class TestApp:

    # @pytest.skip()
    # def test_open_app(self, web_set_up):
    #     pass

    def test_open_idle_fish(self, idle_fish_set_up):
        pass

# def test_should_send_keys_to_search_box_and_then_check_the_value(self, web_set_up):
#     driver = web_set_up
#     search_box_element = driver.find_element_by_id('txt_query_prefill')
#     search_box_element.send_keys('Hello world!')
#
#     on_search_requested_button = driver.find_element_by_id('btn_start_search')
#     on_search_requested_button.click()
#
#     search_text = driver.find_element_by_id('android:id/search_src_text')
#     search_text_value = search_text.text
#
#     assert 'Hello world!' == search_text_value
