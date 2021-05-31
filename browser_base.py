#coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

class HuYaBrowser(object):
    def __init__(self, room_name):
        self.driver = None
        self.chrome_options = None
        self.room_name = room_name
        self.url = 'https://www.huya.com/' + room_name

    def open(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--window-size=1920,1080')
        print('浏览器启动')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.get(self.url)

    def close(self):
        print('浏览器退出')
        self.driver.quit()

    def get_current_page_source(self) -> str:
        return self.driver.page_source