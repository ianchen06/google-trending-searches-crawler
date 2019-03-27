import re
import json

import requests

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

params = (
    ('hl', 'en-US'),
    ('tz', '-480'),
    ('ed', '20190327'),
    ('geo', 'TW'),
    ('ns', '15'),
)

response = requests.get('https://trends.google.com/trends/api/dailytrends', headers=headers, params=params)
response.encoding = 'utf-8'
dd = response.text.split('\n')[1] # Get rid of some weird string a line above the json data..
sss = json.loads(dd, encoding='utf-8')
ff = [s.get('title').get('query') for s in sss.get('default').get('trendingSearchesDays')[0].get('trendingSearches')]
print(ff)
