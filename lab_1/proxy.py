import requests


def check_proxy(url, proxy, delay=3, debug=False):
    with requests.Session() as s:
        try:
            s.get(url, proxies={'http': 'http://'+proxy}, timeout=delay)
            print('\tSuccess connection!')
            s.close()
            return True
        except requests.RequestException as err:
            if debug:
                print('End with ', err)
        except ValueError:
            if debug:
                print('End with ValueError')

        print('\tFail connection!')
        s.close()
        return False


def check_proxy_from_file(url_list, file_path, delay=3, debug=False):
    result_list = []
    proxy_list = []

    file = open(file_path)
    for line in file:
        proxy_list.append(line[:len(line)-1])
    file.close()

    print('Check', len(proxy_list), 'proxy for', len(url_list), 'urls')
    for url in url_list:
        for proxy in proxy_list:
            print('Check', proxy, 'for', url)
            result = check_proxy(url, proxy, delay, debug)
            if result:
                result_list.append(proxy)

    return result_list

