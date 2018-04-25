import json
import re
import time

import lxml
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

from config import *
from cookie import *

def check():
    try:
        if int(TARGET_ID):
            url = 'https://weibo.cn/u/{TARGET_ID}?page={page_num}'
    except:
        url = 'https://weibo.cn/{TARGET_ID}?page={page_num}'
    name = BeautifulSoup(session.get(url.format(TARGET_ID=TARGET_ID, page_num=1),).text, 'lxml').title.text
    if len(name) == 2:
        print('###待爬取的微博id出错!')
        return url, None
    return url, True

def get_wb_quanwen(key_url='comment/FzT85jc6j'):
    url = 'https://weibo.cn/' + key_url
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    txt = soup.select('.ctt')[0].get_text()
    return txt

def get_weibo(page):
    response = session.get(check()[0].format(TARGET_ID=TARGET_ID, page_num=page))
    soup = BeautifulSoup(response.text, 'lxml')
    txt = soup.select('.ctt')
    for t in txt:
        tt = t.get_text() + '\n' + '-' * 20 + '\n'
        if '全文' in tt:
            pattern2 = re.compile('<a href="(.*?)">')
            quanwen_keywords = re.search(pattern2, str(t)).group(1)
            tt = '【长微博】' + get_wb_quanwen(quanwen_keywords) + '\n' + '-' * 20 + '\n'
        yield tt






def main(page_num=1):
    with open('1.txt', 'wb') as code:
        for x in get_weibo(page_num):
            code.write(x)

if __name__ == '__main__':
    pool = Pool()
    session = save_session()
    groups = ([x for x in range(10)])
    if check()[1]:
        pool.map(main, groups)
    pool.close()
    pool.join()           
        
