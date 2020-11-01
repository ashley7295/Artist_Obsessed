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
        test_album = "Lemonade" # Test album name
        test_artist = "Beyonce" # Test artist name
        test_query = {"method" : "album.getinfo", "api_key" : test_key, "artist" : test_artist, "album" : test_album, "format" : "json"} # Test query with parameters 
        test_query_results = cover_art_api.get_album_art(test_album, test_artist) # Obtain test query results
        self.assertEqual(test_query , test_query_results) # Confirm test results equal expected results

    def test_get_image_by_size(self):
        test_url = cover_art_api.url # Obtain url from cover_art_api.py
        r = requests.get(test_url) # Get data from url
        test_images = r.get("album").get("image") # Looks within API’s “images”
        for i in test_images:
            if i.get("size") == size: # Looks for size
                test_image_url = i.get("#text") # Locates size-specific image
                return test_image_url # Returns size-specific image
        expected_url = cover_art_api.get_image_by_size("images" , "size") # Expected cover_art_api.py results
        self.assertEqual(test_image_url , expected_url) # Confirm test results equal expected results

    def test_image_download(self):
        test_url = cover_art_api.url # Obtain url from cover_art_api.py
        r = requests.get(test_url) # Get data from url
        i = Image.open(BytesIO(r.content)) # Open desired cover art image image
        i.save(test_file_name) # Save cover art image as a new file name
        i.show(test_file_name) # Display album cover art to user
        expected = cover_art_api.image_download(cover_art_api.url, cover_art_api.image_download(file_name) # Expected cover_art_api.py results
        self.assertEqual(test_image_download(self), expected) # Confirm test results equal expected results

if __name__ == "__main__":
    unittest.main()
