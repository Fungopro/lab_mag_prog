import requests
import multiprocessing
import re

session = None


def get_session():
    global session
    if not session:
        session = requests.Session()


def check_proxy(proxy):
    get_session()
    try:
        session.get('https://google.com', proxies={'http': 'http://' + proxy}, timeout=5)
        print('Proxy: ' + proxy + ' work')
    except Exception as exc:
        print('Proxy: ' + proxy + ' doesnt work, error: ', exc)
        return False
    return True


def collect_proxy(url):
    with requests.get(url) as res:
        proxys_list = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', res.text)
    return proxys_list


def multi_proc_check_proxy(proxy_list):
    with multiprocessing.Pool(initializer=get_session) as pool:
        res = pool.map(call_check_proxy, proxy_list)
        return list(res)


def call_check_proxy(proxy):
    if check_proxy(proxy):
        return proxy