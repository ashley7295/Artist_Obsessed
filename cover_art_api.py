from io import BytesIO
from PIL import Image
import requests
import shutil
import os
import glob
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

url = f"http://ws.audioscrobbler.com/2.0"
key = os.environ.get("COVER_KEY")

album_input = input("Enter album title: ")
album = f"{album_input}"
artist_input = input("Enter artists title: ")
artist = f"{artist_input}"
query = {"method" : "album.getinfo", "api_key" : key, "artist" : artist, "album" : album, "format" : "json"}
cover_response = requests.get(url, params=query).json()
images = cover_response.get('album').get('image')
pprint(cover_response)

for i in images:
    if i.get("size") == "large":
        image_url = i.get("#text")
        print(image_url)

def image_download(url, file_name):
    r = requests.get(url)
    i = Image.open(BytesIO(r.content))
    i.save(file_name)
    i.show(file_name)

if __name__ == "__main__":
    i_url = image_url
    file = "album_cover.png"
    image_download(i_url, file)
 