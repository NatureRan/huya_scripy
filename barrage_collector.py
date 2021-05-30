#coding:utf-8

from browser_base import HuYaBrowser
from selenium.webdriver.common.by import By
import time, atexit, logging

@atexit.register
def before_exit():
    hu_ya_browser.close()


if __name__ == '__main__':
    hu_ya_browser = HuYaBrowser('ququ1');
    hu_ya_browser.open()
    time.sleep(5)
    # 开始循环获取网页信息
    i = 0
    data_id = 0
    while i < 20:
        i += 1
        time.sleep(1)
        page_source = hu_ya_browser.get_current_page_source()
        # print(page_source)
        li_list = hu_ya_browser.driver.find_elements_by_xpath('//ul[@id="chat-room__list"]/li')
        # print(len(li_list))

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
                    text = li.text
                    msg = text.split(':')
                    print('普通观众弹幕#用户:' + msg[0] + ' 弹幕:' + msg[1])
                elif div_attr == 'msg-nobleEnter':
                    # print('老爷进入直播间信息')
                    pass
                elif div_attr.startswith('msg-nobleSpeak'):
                    text = li.text
                    msg = text.split(':')
                    print('老爷弹幕#用户:' + msg[0] + ' 弹幕:' + msg[1])
                    pass
                else:
                    # print("消息类型未知:" + div_attr + li.text)
                    # input()
                    pass
            except Exception as e:
                logging.warning("异常：" + str(e))
            # print('----------------------------------------------')
