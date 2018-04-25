import json
import re
import time

import lxml
import requests
from bs4 import BeautifulSoup

from config import *
from cookie import *


def get_wb(page):
    try:
        if int(TARGET_ID):
            url = 'https://weibo.cn/u/{TARGET_ID}?page={page_num}'
    except:
        url = 'https://weibo.cn/{TARGET_ID}?page={page_num}'
    name = BeautifulSoup(session.get(url.format(
        TARGET_ID=TARGET_ID, page_num=page),).text, 'lxml').title.text

    if len(name) == 2:
        print('###待爬取的微博id出错!')
    else:
        response = session.get(url.format(TARGET_ID=TARGET_ID, page_num=page))
        soup = BeautifulSoup(response.text, 'lxml')
        txt = soup.select('.ctt')
        for t in txt:
            tt = t.get_text() + '\n' + '-' * 20 + '\n'
            if '全文' in tt:
                pattern2 = re.compile('<a href="(.*?)">')
                try:
                    quanwen_keywords = re.search(
                        pattern2, str(t)).group(1)
                    tt = '【长微博】' + \
                        get_wb_quanwen(quanwen_keywords) + \
                        '\n' + '-' * 20 + '\n'
                except:
                    pass
            print(tt)
    return tt

def get_wb_quanwen(key_url='comment/FzT85jc6j'):
    url = 'https://weibo.cn/' + key_url

    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    txt = soup.select('.ctt')[0].get_text()
    return txt

session = save_session()
get_wb(2)
