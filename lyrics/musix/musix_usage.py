import os
from dotenv import load_dotenv
from Musix import Track, Lyrics

load_dotenv()

api_key = os.getenv("musix_api_key")

lyrics = Lyrics(api_key)
results = lyrics.track_lyrics_get('4809884')
if results.ok and results.status_code == 200:
    result = results.json()
    headers = result.get('message').get('header')
    body = result.get('message').get('body')
    lyrics = body.get('lyrics').get('lyrics_body')
    print(lyrics)



# track = Track(api_key)
# results = track.track_get('4809884')

# results = track.track_search('Believe')
# if results.ok and results.status_code == 200:
#     result = results.json()
#     headers = result.get('message').get('header')
#     body = result.get('message').get('body')

#     print(f"status code: {headers.get('status_code')}")
#     print(f"{headers.get('available')} results available\n\n")

#     track_list = body.get('track_list')
#     for t in track_list:
#         track = t.get('track')
#         print(f"{track.get('track_id')} - {track.get('track_name')} - {track.get('album_name')} - {track.get('artist_name')}")
# else:
#     print(results.status_code)