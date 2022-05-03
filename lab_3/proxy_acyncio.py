import asyncio
import random

import aiohttp as aiohttp
import requests
import multiprocessing
import re


async def check_site(session, url, proxy):
    # print('http://' + proxy)
    async with session.get(url, proxy='http://' + proxy, timeout=5) as s:
        print(await s.text())
        return f"Read {0} from {1}".format(s.text(), url)


async def async_check_proxy(proxy_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in proxy_list:
            task = asyncio.ensure_future(check_site(session, 'https://google.com', i))
            tasks.append(task)
        res = await asyncio.gather(*tasks, return_exceptions=True)
        print(set(res))
        return res


def collect_proxy(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    return proxys_list


if __name__ == '__main__':
    site = 'https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt'
    res = collect_proxy(site)
    ioloop = asyncio.get_event_loop()
    print('Asynchronous:')
    ioloop.run_until_complete(async_check_proxy(res))
    ioloop.close()


