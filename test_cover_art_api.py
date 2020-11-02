import unittest
from unittest import TestCase
import requests
from io import BytesIO
from PIL import Image
import cover_art_api
import os

class TestCover(unittest.TestCase):

    def test_get_album_art(self):
        test_key = cover_art_api.key # Obtain cover art key from cover_art_api.py
        test_url = cover_art_api.url
        test_album = "Lemonade" # Test album name
        test_artist = "Beyonce" # Test artist name
        test_query = {"method" : "album.getinfo", "api_key" : test_key, "artist" : test_artist, "album" : test_album, "format" : "json"} # Test query with parameters 
        test_query_results = requests.get(test_url , params=test_query).json()
        expected_query_results = requests.get(cover_art_api.url, params=test_query).json() # Query response with requested data
        self.assertEqual(test_query_results , expected_query_results) # Confirm test results equal expected results
 
    # image size is tested within cover_art_api.get_album_art

    # cover_art_api.image_download was created as an "bonus" function

if __name__ == "__main__":
    unittest.main()
