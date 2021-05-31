#coding:utf-8

from typing import List
from browser_base import HuYaBrowser
from selenium.webdriver.common.by import By
import time, atexit, logging
from service.user_barrage_service import UserBarrageService

@atexit.register
def before_exit():
    hu_ya_browser.close()

if __name__ == '__main__':
    room = 'ququ1'
    userBarrageService:UserBarrageService = UserBarrageService()
    hu_ya_browser = HuYaBrowser(room);
    hu_ya_browser.open()
    time.sleep(5)
    # 开始循环获取网页信息
    i = 0
    data_id = 0
    while i < 50:
        i += 1
        time.sleep(1)
        page_source = hu_ya_browser.get_current_page_source()
        li_list = hu_ya_browser.driver.find_elements_by_xpath('//ul[@id="chat-room__list"]/li')
        for li in li_list:
            # 往下找div元素
            try:
                data_id_now = int(li.get_attribute('data-id'))
                if data_id >= data_id_now or data_id_now == 0:
                    continue
                data_id = data_id_now
                div = li.find_element(By.TAG_NAME, 'div')
                # print('data_id:' + str(data_id) + div.text)
                div_attr = div.get_attribute('class')
                # print(div_attr)
                # div往下解析每一条弹幕内容
                if div_attr == 'tit-h-send':
                    # print('这是一条礼物')
                    pass

                elif div_attr == 'msg-normal':
                    # 找到用户元素
                    name:str = div.find_element(By.CLASS_NAME, 'J_userMenu').text
                    barrage:List[str] = div.find_element(By.CLASS_NAME, 'msg').text
                    if not barrage:
                        # 弹幕文本为空，可能发送了图片
                        img = div.find_element(By.CLASS_NAME, 'msg').find_element(By.TAG_NAME, 'img')
                        barrage = img.get_attribute('src')
                    print('普通观众弹幕#用户:' + name + ' 弹幕:' + barrage)
                    # 保存入库
                    userBarrageService.saveUserBarrage(room, name, barrage)

                elif div_attr == 'msg-nobleEnter':
                    # print('老爷进入直播间信息')
                    pass

                elif div_attr.startswith('msg-nobleSpeak'):
                    name:str = div.find_element(By.CLASS_NAME, 'J_userMenu').text
                    barrage:List[str] = div.find_element(By.CLASS_NAME, 'msg').text
                    if not barrage:
                        # 弹幕文本为空，可能发送了图片
                        img = div.find_element(By.CLASS_NAME, 'msg').find_element(By.TAG_NAME, 'img')
                        barrage = img.get_attribute('src')
                    print('老爷弹幕#用户:' + name + ' 弹幕:' + barrage)
                    # 保存入库
                    userBarrageService.saveUserBarrage(room, name, barrage)
                    pass

                else:
                    # print("消息类型未知:" + div_attr + li.text)
                    # input()
                    pass

            except Exception as e:
                logging.warning("异常：" + str(e))
            # print('----------------------------------------------')
