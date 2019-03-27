import re
import json
import sys
import datetime

import requests

start_dt = datetime.datetime.today()
days_int = int(sys.argv[1])

headers = {
        'pragma': 'no-cache',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'cache-control': 'no-cache',
        'authority': 'trends.google.com',
        'referer': 'https://trends.google.com/trends/trendingsearches/daily?geo=TW',
        }

params = {
        'hl': 'en-US',
        'tz': '-480',
        'ed': '20190327',
        'geo': 'TW',
        'ns': '15',
        }

for x in range(days_int):
    days = datetime.timedelta(days=x)
    ed = (start_dt - days).strftime("%Y%m%d")
    print(ed)
    params['ed'] = ed

    response = requests.get('https://trends.google.com/trends/api/dailytrends', headers=headers, params=params)
    response.encoding = 'utf-8'
    dd = response.text.split('\n')[1] # Get rid of some weird string a line above the json data..
    sss = json.loads(dd, encoding='utf-8')
    try:
        ff = [s.get('title').get('query') for s in sss.get('default').get('trendingSearchesDays')[0].get('trendingSearches')]
        print(ff)
    except Exception as e:
        print(sss)
        sys.exit(0)
