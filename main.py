#created module to have something in the amster branch

import ui
import bookmarks
from Spotify_API.spotifyAPI import SpotifyAPI
import os



client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

def main():

    ui.program_intro_message()
    perform_menu_selection()

def perform_menu_selection ():

    menu = True


    while menu:
        user_selection = ui.print_menu()
        
        if user_selection == 1:  
            
            artist_name = ui.get_artist_name()
            album_title = ui.get_album_name()
            song_title = ui.get_song_name()

            print_search_results(artist_name, album_title, song_title)

            save = ui.save_bookmark()

            if save == True:
                save_new_bookmark(artist_name, album_title, song_title)
            elif save == False:
                print('Your bookmark will not be saved.')
            

        elif user_selection == 2: 
            bookmarks.get_all_bookmarks()
        elif user_selection == 3: 
            ID = ui.search_by_id()
            bookmarks.delete_by_id(ID)

        elif user_selection == 4: 
            ID = ui.search_by_id()
            bookmarks.delete_by_id(ID)
            pass
        elif user_selection == 5: 
            quit_program()
            menu = False

def quit_program():
    ui.print_message('Bye and thank you!')

def get_spotifyAPI_data(artist):
    spotify = SpotifyAPI(client_id, client_secret)
    followers = spotify.search_artist_data(artist)
    follower_count = spotify.get_follower_count(followers)
    return follower_count

#TODO
#def get_album_artworkAPI_data([ENTER PARAMS NEEDED HERE]):
    #return results

#TODO
#def get_lyricsAPI_data([ENTER PARAMS NEEDED HERE]):
    #return results

def print_search_results(artist_name, album_title, song_title):

    followers = get_spotifyAPI_data(artist_name)
    
    #TODO finish -- code from above functions go here
    #album_art = get_album_artworkAPI_data()
    #lyrics = get_lyricsAPI_data()


    #TODO fill in the print statements below with your variable
   
    print (f'{artist_name} has {followers} followers on spotify')
    #print (f'Here is the album artwork for {album_title}, {album_art}')
    #print (f'Here are the lyrics for {song_title}: ')
    #print (f'{lyrics}')
    pass
    

def save_new_bookmark(artist, album, song):
    
    followers = get_spotifyAPI_data(artist)

    #TODO
    #album_art = get_album_artworkAPI_data()
    #lyrics = get_lyricsAPI_data()

    #bookmarks.add_new_bookmark(artist, album, song, followers, album_art, lyrics)
    pass

if __name__ == '__main__':
    main()