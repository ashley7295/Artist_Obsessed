import unittest
from unittest import TestCase
import requests
from io import BytesIO
from PIL import Image
import cover_art_api
import os

class TestCover(unittest.TestCase):

    def get_image(self):
        test_key = cover_art_api.key
        test_album = "Come Fly With Me"
        test_artist = "Frank Sinatra"
        test_query = {"method" : "album.getinfo", "api_key" : test_key, "artist" : test_artist, "album" : test_album, "format" : "json"}
        test_cover_response = requests.get(cover_art_api.url, params=test_query).json()
        self.assertEqual(cover_art_api.cover_response, self.test_cover_response)
    
    def test_image_download(self):
        self.images = self.test_cover_response.get('album').get('image')
        self.assertEqual(self.test_cover_response, cover_art_api.cover_response)

        pprint(cover_art_api.cover_response)
        pprint(self.test_cover_response)

if __name__ == "__main__":
    unittest.main()
    i_url = image_url
    file = "test_image_download.png"
    test_image_download(i_url, file)
