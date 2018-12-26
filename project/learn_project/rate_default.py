from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import redis
import json

CACHE_STR_KEY = 'boc-service_BOC_RATE_STR'
CACHE_LIST_KEY = 'boc-service_BOC_RATE_LIST'
redis_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

url = "http://srh.bankofchina.com/search/whpj/search.jsp"
Form_Data = {}
Form_Data['erectDate'] = ''
Form_Data['nothing'] = ''
Form_Data['pjname'] = '1316'
data = parse.urlencode(Form_Data).encode('utf-8')
html = request.urlopen(url, data).read()
soup = BeautifulSoup(html, 'html.parser')

div = soup.find('div', attrs={'class': 'BOC_main publish'})
table = div.find('table')
tr = table.find_all('tr')
latest_data = str(tr[1])


def isExist(latest_data):
    is_exist_cache = redis_cache.get(CACHE_STR_KEY)
    if(is_exist_cache == latest_data):  # 缓存数据与最新数据相同
        # print('true')
        return True
    else:  # 缓存数据与最新数据不同
        # print('false')
        redis_cache.set(CACHE_STR_KEY, latest_data)
        redis_cache.delete(CACHE_LIST_KEY)
        return False


cached_data = isExist(latest_data)

if cached_data == False:
    # print('false')
    for index, item in enumerate(tr):
        if 0 == index:
            continue
        td_content = item.find_all('td')
        coin_name = td_content[0].get_text()    # 货币名称
        rate_buy = td_content[1].get_text()     # 现汇买入价
        cash_buy = td_content[2].get_text()     # 现钞买入价
        rate_sell = td_content[3].get_text()    # 现汇卖出价
        cash_sell = td_content[4].get_text()    # 现钞卖出价
        boc_convert = td_content[5].get_text()  # 中行折算价
        create_time = td_content[6].get_text()  # 发布时间

        cache = json.dumps({
            'coin_name': coin_name,
            'rate_buy': rate_buy,
            'cash_buy': cash_buy,
            'rate_sell': rate_sell,
            'cash_sell': cash_sell,
            'boc_convert': boc_convert,
            'create_time': create_time
        })

        redis_cache.lpush(CACHE_LIST_KEY, cache)
