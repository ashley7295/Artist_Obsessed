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

#function that calls bookmarks.py to display all bookmarks
def display_all_bookmarks():
    bookmarks.get_all_bookmarks()
    
#validates if search_by_ID is returning NONE and will print a message to the user, otherwise prints the bookmark
def search_for_bookmark_by_id():
    ID = ui.search_by_id()
    get_by_id = bookmarks.search_by_id(ID)

    if get_by_id == None:
        print('There is not a bookmark that contains this ID')
    else:
        print ('\n', get_by_id, '\n')

#validtes that delete_by_ID is returning NONE and will print a message to the user, otherwise validates the bookmark was deleted
def delete_bookmark():
    ID = ui.search_by_id()
    delete_by_id = bookmarks.delete_by_id(ID)

    if delete_by_id == None:
        print('There is not a bookmark that contains this ID')
    else:
        print(f'\n', 'Your bookmark with bookmark ID:', ID, 'has been deleted', '\n')

#ends the program
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

def search_artwork(artist, album): # Obtains album cover artwork via cover_art_api.py
    return cover_art_api.get_album_art(artist, album) # Returns cover art, if found

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
    save = ui.save_bookmark()

    if save == True:
        save_new_bookmark(results)
    else:
        print('Okay this bookmark will not be saved')



def print_search_results(results):
    print("\n")
    print(f"{results.get('artist_name')} has {results.get('follower_count')} followers on spotify")
    print(f"Here is the album artwork for {results.get('album_title')}: {results.get('artwork')}")
    print("*if the photo does not automatically open, press CMD+CLICK on the url to view in your browser")
    print(f"Here are the lyrics for {results.get('song_title')}:", "\n") 
    print(results.get('lyrics'))
    print("\n")

def save_new_bookmark(results):
    
    artist = results.get('artist_name')
    album = results.get('album_title')
    song = results.get('song_title')
    followers = results.get('follower_count')
    album_art = results.get('artwork')
    lyrics = results.get('lyrics')

    bookmarks.add_new_bookmark(artist, album, song, followers, album_art, lyrics)
    print('Your Bookmark has been saved!')
    

if __name__ == '__main__':
    main()


