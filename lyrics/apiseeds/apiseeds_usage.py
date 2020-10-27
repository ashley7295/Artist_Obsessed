import os
from dotenv import load_dotenv
from Apiseeds import Apiseeds

load_dotenv()

api_key = os.getenv("apiseeds_api_key")

apiseeds = Apiseeds(api_key)

response = apiseeds.get_lyrics('kanye west', 'monster')

if response.ok and response.status_code == 200:
    r = response.json().get('result')
    artist = r.get('artist')
    track = r.get('track')
    print(artist['name'])
    print(track['name'], track['text'])
else:
    print(response.status_code)