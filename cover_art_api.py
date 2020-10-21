from PIL import Image
import shutil
import requests
import os
import glob
from pprint import pprint

url = f"http://ws.audioscrobbler.com/2.0"
#key = os.environ.get("COVER_KEY") # "2066002fabe29cf09d7ed5a00c804ac6"
key = "2066002fabe29cf09d7ed5a00c804ac6"
print(key)

album_input = input("Enter album title: ")
album = f"{album_input}"
query = {"method" : "album.getinfo", "api_key" : key, "artist" : "Cher", "album" : album, "format" : "json"}
cover_response = requests.get(url, params=query).json()
pprint(cover_response)

# "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=2066002fabe29cf09d7ed5a00c804ac6&artist=Cher&album=Believe&format=json"

# album_art = cover_response["album"]

# for art in album_art:
    # cover_art = art["image"][2]

# For image saving / future pillow use
# if r.status_code == 200:
    # cover_reponse.raw.decode_content = True
    # 
    # with open(filename, "wb") as f:
        # shutil.copyfileobj(cover_respose.raw, f)
    # print(filename, " was successfully downloaded.")
    # filename.show()
# else:
    # print("The requested image could not be found.")
