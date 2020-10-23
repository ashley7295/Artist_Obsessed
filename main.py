#created module to have something in the master branch
import os

from Spotify_API.spotifyAPI import SpotifyAPI


client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

spotify = SpotifyAPI(client_id, client_secret)

def main():
    #replace this and use where needed once UI and Menu are created
    data = spotify.search_artist_data('beyonce')
    followers = spotify.get_follower_count(data)
    print(followers) 



if __name__ == '__main__':
    main()
