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

    def test_get_image_by_size(self):
        r = requests.get(cover_art_api.url) # Obtain url from cover_art_api.py
        test_images = r.get("album").get("image") # Looks within API’s “images”
        for i in test_images:
            # size variable below has squigglies as "undefined variable"
            if i.get("size") == size: # Looks for specific image size
                test_image_url = i.get("#text") # Locates size-specific image
                return test_image_url # Returns size-specific image
        expected_url = cover_art_api.get_image_by_size("images" , "size") # Expected cover_art_api.py results
        self.assertEqual(test_image_url , expected_url) # Confirm test results equal expected results

    def test_image_download(self):
        testValue = True # Set test value to True for future data comparison
        r = requests.get(cover_art_api.url) # Obtain url from cover_art_api.py
        i = Image.open(BytesIO(r.content)) # Open desired cover art image image
        test_file_name = "test_image_download.png" # Assign file name
        save = i.save(test_file_name) # Save cover art image as a assigned file name
        show = i.show(test_file_name) # Display album cover art to user
        self.assertTrue(testValue , show) # Confirm test results equal expected results
        self.assertTrue(testValue , save) # Confirm test results equal expected results

if __name__ == "__main__":
    unittest.main()
