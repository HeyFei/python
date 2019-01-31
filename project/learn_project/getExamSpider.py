# -*- coding: utf-8 -*-
# Your code goes below this line

import requests
import json
from bs4 import BeautifulSoup


class Getepic:
    def __init__(self, username, password):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'http://passport.233.com/login',
            'Host': 'passport.233.com'
        }
        self.login_url = 'http://passport.233.com/login'
        self.post_url = 'http://passport.233.com/api/singin'
        self.get_exam_url = 'http://wx.233.com/tiku/paper/do/49c1afa739fdfcaddaa83e5f1f96c2f4?mode=2&paperType=3&fromUrl=http://wx.233.com/tiku/exam/214?paperType=3'
        self.session = requests.session()
        self.username = username
        self.password = password

    def login(self):
        post_data = self.get_post_data()
        headers = self.headers.copy()
        response = self.session.post(self.post_url, data=post_data, headers=headers)
        data = json.loads(response.content.decode('utf-8'))
        print(str(data))
        #print(unicode(response.text, 'utf-8'))
        # print(("cañete").encode('utf8'))
        quit()
        if(data['result'] == None):
            return False
        else:
            return data['result']


if __name__ == '__main__':
    #username = "13024170887"
    #password = "xueersen"
    username = "18358170207"
    password = "sjm000000"

    getepic = Getepic(username, password)
    data = getepic.login()
    if data:
        getepic.choose_profile()
    else:
        print('Oops, login failed!')
        quit()
