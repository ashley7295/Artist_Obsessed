from PIL import Image
import shutil
import requests
import os
import glob
from pprint import pprint

cover = Image.open("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/golden_gate.jpg") # Existing image opened from directory folder

# cover.show() # Displays directory image to user via their machine's default image viewer
cover.save("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/saved_cover.jpg") # Saves image opened from directory as a "displayed image"
cover.show()
