from concurrent.futures import ThreadPoolExecutor

import requests


def check_proxy(url_proxy, delay=5, debug=True):
    with requests.Session() as s:
        try:
            print('Check', url_proxy[1], 'for', url_proxy[0])
            s.get(url_proxy[0], proxies={'http': 'http://'+url_proxy[1]}, timeout=delay)
            print('\tSuccess connection!', url_proxy[1], 'for', url_proxy[0])
            s.close()
            return True
        except requests.RequestException as err:
            if debug:
                print('End with ', err)
        except ValueError:
            if debug:
                print('End with ValueError')

        s.close()
        return False


def check_proxy_from_file(url_list, file_path):
    result_list = []
    proxy_list = []

    file = open(file_path)
    for line in file:
        proxy_list.append(line[:len(line)-1])
    file.close()

    print('Check', len(proxy_list), 'proxy for', len(url_list), 'urls')
    for url in url_list:
        proxy_arr = list(map(lambda x: (url, x), proxy_list))
        with ThreadPoolExecutor(max_workers=16) as executor:
            try:
                results = executor.map(check_proxy, proxy_arr)
            except Exception as exc:
                print('Exc: ', exc)
        print(results)
    return result_list

