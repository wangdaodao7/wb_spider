import json
import re
import time

import lxml
import requests
from bs4 import BeautifulSoup

from config import *
from cookie import *


def get_wb():
    try:
        if int(TARGET_ID):
            url = 'https://weibo.cn/u/{TARGET_ID}?page={page_num}'
    except:
        url = 'https://weibo.cn/{TARGET_ID}?page={page_num}'
    name = BeautifulSoup(session.get(url.format(
        TARGET_ID=TARGET_ID, page_num=1),).text, 'lxml').title.text

    if len(name) == 2:
        print('###微博id出错!')
    else:
        with open('{}.txt'.format(name), 'w', encoding='utf-8') as code:
            for x in range(1, MAX_PAGES):
                response = session.get(url.format(
                    TARGET_ID=TARGET_ID, page_num=str(x)))
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
                    code.write(tt)


def get_wb_quanwen(key_url='comment/FzT85jc6j'):
    url = 'https://weibo.cn/' + key_url

    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    txt = soup.select('.ctt')[0].get_text()
    return txt

session = wb_session()
