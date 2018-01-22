
import requests
import lxml
import re
import json
from bs4 import BeautifulSoup
from config import *

login_url = 'https://passport.weibo.cn/sso/login'
session = requests.Session()
login = session.post(login_url, data=data, headers=headers)
response = session.get('https://www.weibo.cn')

 
def check():
    pass

def wb_session():
    if response.status_code == 200:
        tips = json.loads(login.text)
        if tips.get('retcode') == 20000000:
            pattern = re.compile('class="ut">(.*?)<a')
            hello = re.search(pattern, response.text).group(1)
            print('登录成功：欢迎您，{0}！'.format(hello))
            return session
        elif tips.get('retcode') == 50011015:
            print('id', tips.get('msg'))
            return None
        elif tips.get('retcode') == 50011002:
            print('password', tips.get('msg'))
            return None
        elif tips.get('retcode') == 50011005:
            print(tips.get('msg'))
            return None
    else:
        print('登录失败！问题是:{}。'.format(response.status_code))
