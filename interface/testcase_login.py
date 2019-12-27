import unittest
import requests
import os
import sys
from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://192.168.75.169:8090/CadreSystem/api/login"

    def tearDown(self):
        print(self.result)

    def test_login(self):
        payload = {"username": "ganbu", "password": "123456"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 1)


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()
