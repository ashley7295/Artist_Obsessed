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

url = f"http://ws.audioscrobbler.com/2.0" # API site URL
key = os.environ.get("COVER_KEY") # Link to API key

def get_album_art(artist, album): # Searches for album artwork from API query results
    query = {"method" : "album.getinfo", "api_key" : key, "artist" : artist, "album" : album, "format" : "json"} # Query with parameters to locate a specific album
    try:
        cover_response = requests.get(url, params=query).json() # Query response with requested data
        images = cover_response.get('album').get('image') # Looks within API’s “images”
        return get_image_by_size(images, 'large') # If large image API option available, return
    except Exception as err:
        logging.error(err) # Error if not found
        return "Could not find artwork" # Display error reason to user

def get_image_by_size(images, size): # Searches for album art by size specifications     
    for i in images: # Looks within API’s “images”     
        if i.get("size") == size: # Looks for size         
            image_url = i.get("#text") # Locates size-specific image           
            return image_url # Returns size-specific image url

# Function not required as part of current program. May be a useful function in future.
def image_download(url, file_name): # Save and displays image for user
    r = requests.get(url) # Open url
    i = Image.open(BytesIO(r.content)) # Open desired cover art image image
    i.save(file_name) # Save cover art image as a new file name
    i.show(file_name) # Display album cover art to user
