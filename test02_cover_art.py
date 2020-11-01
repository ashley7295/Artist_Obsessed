import unittest
from unittest import TestCase
import requests
from io import BytesIO
from PIL import Image
import cover_art_api
import os

class TestCover(unittest.TestCase):

    def test_get_album_art(self):
        test_key = cover_art_api.key
        test_album = "Lemonade"
        test_artist = "Beyonce"
        test_query = {"method" : "album.getinfo", "api_key" : test_key, "artist" : test_artist, "album" : test_album, "format" : "json"}
        test_query_results = cover_art_api.get_album_art(test_album, test_artist)
        self.assertEqual(test_query , test_query_results)

    def test_get_image_by_size(self):
        test_url = cover_art_api.url
        r = requests.get(test_url)
        test_images = r.get("album").get("image")
        for i in test_images:
            if i.get("size") == size:
                test_image_url = i.get("#text")
                return test_image_url
        expected_url = cover_art_api.get_image_by_size("images" , "size")
        self.assertEqual(test_image_url , expected_url)

    def test_image_download(self):
        test_url = cover_art_api.url
        r = requests.get(test_url)
        i = Image.open(BytesIO(r.content))
        ei = cover_art_api.image_download.Image.open(BytesIO(r.content))
        i.save(test_file_name)
        i.show(test_file_name)
        self.assertEqual(i , ei)
        self.assertEqual(i.save(test_file_name) , cover_art_api.i.save(test_file_name))
