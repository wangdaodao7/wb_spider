import json
import re,time

import lxml
import requests
from bs4 import BeautifulSoup

from config import *
from cookie import wb_session




session = wb_session()

def get_f():
    url = 'https://weibo.cn/comment/FD9C95GfD?rl=1&page={page_num}'
    # url = 'https://weibo.cn/comment/F0rAj8KRg?uid=3816914843&rl=0&page={page_num}'

    xxx = []
    
    for x in range(5000, 24831):
        if session:
            response = session.get(url.format(page_num=str(x)))
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            # print(response.text)
            if response.status_code == 403:
                print('访问频繁，等重试！')
                time.sleep(300)
                x = x - 1
                
            
            txt = soup.select('.ctt')

            with open('13.txt', 'a') as code:
                for t in txt:
                    # print(t.get_text())
                    if '22' in t.get_text():
                        print('-----第{0}页----------'.format(x),t.get_text(), '---------------------')
                        code.write( str(x) +'\n')
                    if  '06.22' in t.get_text():
                        print('-----第{0}页----------'.format(x),t.get_text(), '---------------------')
                        code.write(  str(x) + t.get_text() +'\n')
                    if '06/22' in t.get_text():
                        print('----第{0}页-----------'.format(x),t.get_text(), '---------------------')
                        code.write(str(x) + t.get_text() +'\n')
                    if '6.22' in t.get_text():
                        print('----第{0}页-----------'.format(x),t.get_text(), '---------------------')
                        code.write( str(x) + t.get_text() +'\n')
                    if '622' in t.get_text():
                        print('----第{0}页-----------'.format(x),t.get_text(), '---------------------')
                        code.write( str(x) + t.get_text() +'\n')
            print('第{}页查询完毕！'.format(x))
            time.sleep(1)
            
        
   


# get_f()
