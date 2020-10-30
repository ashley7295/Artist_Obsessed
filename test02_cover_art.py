import unittest
from unittest import TestCase
import requests
from io import BytesIO
from PIL import Image
import cover_art_api
import os

class TestCover(unittest.TestCase):

    def test_data(self):
        test_key = cover_art_api.key
        test_album = "Lemonade"
        test_artist = "Beyonce"
        test_query = {"method" : "album.getinfo", "api_key" : test_key, "artist" : test_artist, "album" : test_album, "format" : "json"}
        test_query_results = cover_art_api.data(test_album,test_artist)
        self.assertEqual(test_query , test_query_results)

    # def test_data_02(self):
    #     test_cover_response = requests.get(cover_art_api.url, params=test_query).json()
    #     test_images = test_cover_response.get("album").get("image")
    #     self.assertEqual(test_cover_response, cover_art_api.cover_response)

#         for i in test_images:
#             if i.get("size") == "large":
#                 test_image_url = i.get("#text")
#                 print(test_image_url)
#                 self.assertEqual(test_image_url, cover_art_api.image_url)

if __name__ == "__main__":
    unittest.main()
#     test_image_url = i_url
#     file = "test_image_download.png"
#     test_image_download(i_url, file)
#     unittest.main()
