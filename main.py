import ui
import os
import bookmarks
from menu import Menu
from Spotify_API.spotifyAPI import SpotifyAPI
from dotenv import load_dotenv
from apiseeds.Apiseeds import Apiseeds
import cover_art_api

def main():
    load_dotenv()
    menu = Menu()
    setup_menu(menu)
    ui.program_intro_message()
    while True:
        ui.print_message(menu)
        selection = ui.get_int_in_range('', 1, menu.get_menu_length())
        action = menu.get_option(selection)
        action()

def setup_menu(menu):
    menu.add(1, 'Start Search query', search)
    menu.add(2, 'Display all Bookmarks', display_all_bookmarks)
    menu.add(3, 'Search for a bookmark by ID', search_for_bookmark_by_id)
    menu.add(4, 'Delete a Bookmark by ID', delete_bookmark)
    menu.add(5, 'Quit', quit_program)

def display_all_bookmarks():
    # bookmarks.get_all_bookmarks()
    pass

def search_for_bookmark_by_id():
    pass

def delete_bookmark():
    # ID = ui.search_by_id()
    # bookmarks.delete_by_id(ID)
    pass

def quit_program():
    ui.print_message('Bye and thank you!')
    exit()

def search_spotify(artist):
    """
    @param string artist: artist to search for
    @returns int: follower count
    """
    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
    
    spotify = SpotifyAPI(client_id, client_secret)

    data = spotify.search_artist_data(artist)
    followers = spotify.get_follower_count(data)
    
    return followers

def search_artwork(artist, album):
    """
    @param string artist: artist to search for
    @returns string: image url
    """
    cover_artist = 
    x = cover_art_api.
    return cover_art_api.get_album_art(artist, album)

def search_lyrics(artist, song_name):
    """
    @param string artist: artist to search for
    @param string song_name: song_name to search for
    @returns string: the lyrics or False if not found
    """

    api_key = os.getenv("APISEEDS_KEY")
    apiseeds = Apiseeds(api_key)

    response = apiseeds.get_lyrics(artist, song_name)

    if response.ok and response.status_code == 200:
        r = response.json().get('result')
        track = r.get('track')
        return track['text']
    else:
        print(response.status_code)
        return 'Lyrics not found.'

def search():
    """
    #gets variables for the UI of the search queries

    """
    artist_name = ui.get_string('What is the name of the artist you are searching for?: ')
    album_title = ui.get_string('What is the name of the album you are looking for?: ')
    song_title = ui.get_string('What is the name of the song you are looking for?: ')
    follower_count = search_spotify(artist_name)
    lyrics = search_lyrics(artist_name, song_title)
    artwork = search_artwork(artist_name, album_title)

    results = {
        'artist_name': artist_name,
        'album_title': album_title,
        'song_title': song_title,
        'artwork': artwork,
        'lyrics': lyrics,
        'follower_count': follower_count
    }
    print_search_results(results)

def print_search_results(results):
    print(f"{results.get('artist_name')} has {results.get('follower_count')} followers on spotify")
    print(f"Here is the album artwork for {results.get('album_title')}, {results.get('artwork')}")
    print(f"Here are the lyrics for {results.get('song_title')}:") 
    print(results.get('lyrics'))

def save_new_bookmark():
    #TODO once search_results() function can be finished this one can be filled in as well

    #artist, album, song = user_search()
    #followers, album_art, lyrics = search_results()

    #bookmarks.add_new_bookmark(artist, album, song, followers, album_art, lyrics)
    pass

if __name__ == '__main__':
    main()


