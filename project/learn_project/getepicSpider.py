import requests
import json
from bs4 import BeautifulSoup


class Getepic:
    def __init__(self, username, password):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://www.getepic.com/app/sign_in'
        }
        self.login_url = 'https://www.getepic.com/app/sign_in'
        self.post_url = 'https://www.getepic.com/webapi/index.php?class=WebAccount&method=noAuthLogin'
        self.get_profile_url = 'https://www.getepic.com/webapi/index.php?class=WebAccount&method=getProfiles&dev=web&includeStats=1'  # get three role
        self.get_books_url = 'https://www.getepic.com/webapi/index.php?class=WebCategory&method=getContentRowsForSection&dev=web&sectionId=1&time=2019-01-11%2015%3A10%20%2B0000'
        self.session = requests.session()
        self.username = username
        self.password = password

    def get_post_data(self):
        data = {
            'dev': 'web',
            'email': self.username,
            'pass': self.password
        }
        return data

    def choose_profile(self):
        headers = self.headers.copy()
        html = self.session.get(self.get_profile_url, headers=headers)
        print(html.text)

    def login(self):
        post_data = self.get_post_data()
        headers = self.headers.copy()
        response = self.session.post(self.post_url, data=post_data, headers=headers)
        data = json.loads(response.content.decode('utf-8'))
        if(data['result'] == None):
            return False
        else:
            return data['result']


if __name__ == '__main__':
    username = input("Enter Email Address:")
    password = input("Enter your Password:")

    getepic = Getepic(username, password)
    data = getepic.login()
    if data:
        getepic.choose_profile()
    else:
        print('Oops, login failed!')
        exit()
