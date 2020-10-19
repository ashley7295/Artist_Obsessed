import unittest
from cache import Cache


class TestCache(unittest.TestCase):
    def test_setting(self):
        cache = Cache()
        service_response = {'response': []}
        key = 'service1'
        b64d_url = 'abcdef'
        cache.set(key, b64d_url , service_response, 30)
        cached_response = cache.get(key, b64d_url)
        self.assertEqual(service_response, cached_response.get('value'))



if __name__ == "__main__":
    unittest.main()
