import os
from dotenv import load_dotenv
from Musix import Track

load_dotenv()

api_key = os.getenv("musix_api_key")

track = Track(api_key)

results = track.track_search('Believe')
if results.ok and results.status_code == 200:
    headers = results.get('message').get('header')
    body = results.get('message').get('body')

    print(f"status code: {headers.get('status_code')}")
    print(f"{headers.get('available')} results available\n\n")

    track_list = body.get('track_list')
    for t in track_list:
        track = t.get('track')
        print(f"{track.get('track_id')} - {track.get('track_name')} - {track.get('album_name')} {track.get('artist_name')}")
else:
    print(results.status_code)