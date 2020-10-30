import unittest
from unittest import TestCase
from io import BytesIO
from PIL import Image
import shutil
import requests
import os
from pprint import pprint
import cover_art_api

test_url = cover_art_api.url
test_key = cover_art_api.key
cover_response = cover_art_api.cover_response
test_cover_response = test_image_download.r

def test_image_download(self):
    r = requests.get(test_url)
    i = Image.open(BytesIO(r.content))
    i.save(test_file_name)
    i.show(test_file_name)
    self.assertEqual(cover_art_api.cover_response , test_cover_response)

if __name__ == "__main__":
    t_url = test_cover_response.image_url
    file = "test_image_download.png"
    test_image_download(t_url, file)
