import unittest
import time

from lab_1.proxy import check_proxy_from_file

PROXY_LIST = './proxy.txt'

# @unittest.skip
class TestProxyChecker(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def test(self):
        site_list = [
            'http://www.google.com/',
            'http://www.yandex.com/'
        ]

        self.res = check_proxy_from_file(site_list, PROXY_LIST)
        self.assertEqual(len(self.res), len(self.res))

    def tearDown(self):
        duration = time.time() - self.start_time
        print(f"{self.id}: End with {len(self.res)} proxy in {duration} seconds")