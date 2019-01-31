from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import urllib.request
#import ssh

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter -')
url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find('a')
tagss = soup('a')
print(type(tags))
for tag in tags:
    print(tag)
