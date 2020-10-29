import unittest
from cache import Cache


class TestCache(unittest.TestCase):


    def setUp(self):
        """
        create a new cache for each test overwriting previous self.cache state
        """
        self.service_response = {'response': []}
        self.key = 'service1'
        self.b64d_url = 'abcdef'
        self.cache = Cache()
        self.cache.set(self.key, self.b64d_url , self.service_response, 30)


    def test_setting(self):
        cached_response = self.cache.get(self.key, self.b64d_url)
        self.assertEqual(self.service_response, cached_response.get('value'))

    def test_invalidating(self):
        self.cache.set('somekey2','vavagw',{'f':1}, 30)
        self.cache.invalidate(self.key)
        storage = self.cache.storage
        self.assertEqual(storage, {'somekey2': {'vavagw': {'expiration': 30, 'value': {'f': 1}}}})

    def test_invalid_keys(self):
        # TODO add test for when a key is requested and is invalid
        pass

if __name__ == "__main__":
    unittest.main()
