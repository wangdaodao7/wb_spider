import requests
import lxml
import re
import json
from bs4 import BeautifulSoup




LOGIN_ID = '131423824239'
LOGIN_PASSWORD = '11111111a'

login_url = 'https://passport.weibo.cn/sso/login'


session = requests.Session()




headers = {   
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'172',
    'Content-Type':'application/x-www-form-urlencoded',
    # 'Cookie':'_T_WM=8135db08211080e91893add0932aea24; SCF=AobFkzK_RIPlkH6rYNkYePHj4d2WLFFqp0EfeNKysrkOdqbH9d_HlF_JW2ivd-Ruu2ElLV2PFVJvuRKEyIChKl8.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWHd4cz8YK0W1r4JKwMA8aX5JpX5KMhUgL.Fo-XSozXSo-0SKn2dJLoIXnLxKqL122LBo2LxKML1-BL1h5LxKML12eLB-zLxK-L1KzLB-2LxK-L12-LB.zLxKnLB.qL1-eLxKqL1KqLBo.LxKML1-2L1hBt; login=2539a3746215f32d05c8100e941e1569; SUHB=0k1DvVUOxYpPwv; SUB=_2AkMtD4NWdcPxrAJWmfgUym3hZIxH-jye2uqgAn7oJhMyPRh77nUuqSdutBF-XIOhiQvHIWrh8F7YO7xfS-Tv8Qcm',
    'Host':'passport.weibo.cn',
    'Origin':'https://passport.weibo.cn',
    'Pragma':'no-cache',
    'Referer':'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.7.12777.400'
}


data = {
    'username': LOGIN_ID,
    'password': LOGIN_PASSWORD,
    'savestate': '1',
    'r': 'http://weibo.cn/',
    'ec': '1',
    'pagerefer': '',
    'entry': 'mweibo',
    'wentry': '',
    'loginfrom': '',
    'client_id': '',
    'code': '',
    'qq': '',
    'mainpageflag': '1',
    'hff': '',
    'hfp': '',
}


login = session.post(login_url, data=data, headers=headers)
response = session.get('https://www.weibo.cn')


def wb_session():
    
    if response.status_code == 200:
        tips = json.loads(login.text)
        # print(tips)
        # print(tips.get('retcode'))
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
        
        # print(response.text)
        print('登录失败！问题是:{}。'.format(response.status_code))


wb_session()