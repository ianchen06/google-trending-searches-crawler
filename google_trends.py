import json
import sys
import datetime
import asyncio

import aiohttp

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

data = []

def parse(html):
    dd = html.split('\n')[1] # Get rid of some weird string a line above the json data..
    sss = json.loads(dd, encoding='utf-8')
    try:
        ff = [s.get('title').get('query') for s in sss.get('default').get('trendingSearchesDays')[0].get('trendingSearches')]
    except Exception as e:
        print(sss)
        sys.exit(0)
    return ff

async def fetch(session, url, headers, params):
    print(f"fetching {url}")
    async with session.get(url, headers=headers, params=params) as response:
        return await response.text()

async def main():
    futs = []
    async with aiohttp.ClientSession() as session:
        for x in range(days_int):
            days = datetime.timedelta(days=x)
            ed = (start_dt - days).strftime("%Y%m%d")
            print(ed)
            params['ed'] = ed
            futs.append(fetch(session, 'https://trends.google.com/trends/api/dailytrends', headers=headers, params=params))
        htmls = await asyncio.gather(*futs)
        for html in htmls:
            data.extend(parse(html))
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
