from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import urllib.request
import logging
import redis
import json
import sys
import codecs

logging.basicConfig(
    filename="console.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

CACHE_STR_KEY = 'boc-service_BOC_RATE_STR_USDT'
CACHE_LIST_KEY = 'boc-service_BOC_RATE_LIST_USDT'
redis_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)


class Spier:

    def __init__(self, url):
        self.url = url

    def getHtml(self):
        print('req_open_html begin')
        try:
            params = {
                'erectDate': '',
                'nothing': '',
                'pjname': '1316',
            }
            post_args = parse.urlencode(params).encode('utf-8')
            html = request.urlopen(self.url, post_args).read()
        except urllib.error.HTTPError as e:
            return e.code
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                return e.code
            if hasattr(e, "reason"):
                return e.reason
            else:
                return 'OK'
        else:
            return html

    def isCached(latest_data):
        is_exist_cache = redis_cache.get(CACHE_STR_KEY)
        if(is_exist_cache == latest_data):  # 缓存数据与最新数据相同
            # print('true')
            return True
        else:  # 缓存数据与最新数据不同
            # print('false')
            redis_cache.set(CACHE_STR_KEY, latest_data)
            redis_cache.delete(CACHE_LIST_KEY)
        return False

    def writeCache(self, html):
        redis_cache.delete(CACHE_LIST_KEY)
        html = html[1:-1]
        for index, item in enumerate(html):
            td_content = item.find_all('td')
            coin_name = td_content[0].get_text()  # 货币名称
            rate_buy = td_content[1].get_text()  # 现汇买入价
            cash_buy = td_content[2].get_text()  # 现钞买入价
            rate_sell = td_content[3].get_text()  # 现汇卖出价
            cash_sell = td_content[4].get_text()  # 现钞卖出价
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
        return True

    def arithmeticalMean(self, cached_convert, latest_convert):
        cached_convert = float(cached_convert)
        latest_convert = float(latest_convert)
        result = (cached_convert + latest_convert) / 2
        if (abs(result - cached_convert)) / 100 < 0.1 or (abs(result - latest_convert)) / 100 < 0.1:
            return False
        else:
            return True


if __name__ == '__main__':
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp'
    spider = Spier(url)
    html = spider.getHtml()
    print('parse html begin')
    if isinstance(html, int) or 'OK' == html:
        logging.debug(html)
        exit(-1)

    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class': 'BOC_main publish'})
    table = div.find('table')
    tr = table.find_all('tr')
    latest_data_str = str(tr[1])

    latest_data = tr[1]
    latest_td = latest_data.find_all('td')
    latest_data_dist = {
        'coin_name': latest_td[0].get_text(),
        'rate_buy': latest_td[1].get_text(),
        'cash_buy': latest_td[2].get_text(),
        'rate_sell': latest_td[3].get_text(),
        'cash_sell': latest_td[4].get_text(),
        'boc_convert': latest_td[5].get_text(),
        'create_time': latest_td[6].get_text()
    }
    latest_convert = latest_td[5].get_text()

    # 获取缓存中的数据
    cached_data = redis_cache.get(CACHE_STR_KEY)
    if cached_data != None:
        cached_data = json.loads(redis_cache.get(CACHE_STR_KEY))
        cached_convert = cached_data['boc_convert']
        # print(type(cached_convert),cached_convert,"\n")
        # print(type(latest_convert),latest_convert,"\n")
        if(spider.arithmeticalMean(cached_convert, latest_convert)):
            logging.debug('数据异常')
            exit(-1)
        if cached_convert == latest_convert:
            logging.debug('same')
            exit(-1)

    redis_cache.set(CACHE_STR_KEY, json.dumps(latest_data_dist))
    spider.writeCache(tr)
