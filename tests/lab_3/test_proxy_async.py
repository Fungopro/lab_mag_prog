import asyncio
import unittest
import time

from lab_3.proxy_acyncio import collect_proxy, async_check_proxy


class TestLab3(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()

    def test_collect_proxy(self):
        self.site = 'https://github.com/ShiftyTR/Proxy-List/blob/master/proxy.txt'
        res = collect_proxy(self.site)
        self.assertTrue(len(res) != 0)
        print('Asynchronous:')
        async_check_proxy(res)


    def tearDown(self) -> None:
        duration = time.time() - self.start_time
        print(f'{self.id()}: checked proxies in {duration} seconds')

