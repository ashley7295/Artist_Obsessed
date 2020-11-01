from io import BytesIO
from PIL import Image
import requests
import shutil
import os
import glob
from pprint import pprint
from dotenv import load_dotenv
import logging

load_dotenv()

url = f"http://ws.audioscrobbler.com/2.0"
key = os.environ.get("COVER_KEY")
<<<<<<< HEAD
=======

>>>>>>> 65ff8745024b3b9dbada5db2d55dd96e40584f9c

def get_album_art(artist, album):
    query = {"method" : "album.getinfo", "api_key" : key, "artist" : artist, "album" : album, "format" : "json"}
    try:
        cover_response = requests.get(url, params=query).json()
        images = cover_response.get('album').get('image')
        return get_image_by_size(images, 'large')
    except Exception as err:
        logging.error(err)
        return "Could not find artwork"

def get_image_by_size(images, size):
    for i in images:
        if i.get("size") == size:
            image_url = i.get("#text")
            return image_url

 def image_download(url, file_name):
     r = requests.get(url)
     i = Image.open(BytesIO(r.content))
     i.save(file_name)
     i.show(file_name)
