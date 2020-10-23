#created module to have something in the amster branch

import ui
import bookmarks

def main():

    ui.program_intro_message()
    preform_menu_selection()

def preform_menu_selection ():

    menu = True


    while menu:
        user_selection = ui.print_menu()
        
        if user_selection == 1:  
            
            user_search()
            print_search_results()

            save = ui.save_bookmark()

            if save == True:
                save_new_bookmark()
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


def search_results():
    #TODO set variables for results of our APIs

    #followers = SpotifyAPI
    #album_artwork = artworkAPI
    #lyrics = lyricsAPI
    
    #return followers, album_artwork, lyrics
    pass

#gets variables for the UI of the search queries
def user_search():
    artist_name = ui.get_artist_name()
    album_title = ui.get_album_name()
    song_title = ui.get_song_name()
    return artist_name, album_title, song_title


def print_search_results():
    #TODO once we can finish the search_results() function, we can finish this one
    
    #artist, album, song = user_search()
    #followers, album_art, lyrics = search_results()
    
    #print = {artist} has {followers} followers on spotify
    #print = Here is the album artwork for {album}, {album_art}
    #print = Here are the lyrics for {song}: 
    #print = {lyrics}
    pass
    

def save_new_bookmark():
    #TODO once search_results() function can be finished this one can be filled in as well

    #artist, album, song = user_search()
    #followers, album_art, lyrics = search_results()

    #bookmarks.add_new_bookmark(artist, album, song, followers, album_art, lyrics)
    pass

if __name__ == '__main__':
    main()
