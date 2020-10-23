#created module to have something in the amster branch

import ui
import bookmarks


def preform_menu_selection ():

    menu = True


    while menu:
        user_selection = ui.print_menu()
        
        if user_selection == 1:  
        #enter display bookmarks function
            pass    
        elif user_selection == 2: 
            ui.get_artist_name
            ui.get_album_name
            ui.get_song_name
            
            search_results()

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
    ui.print_message('Bye and Thank you!')

def search_results():
    #print = {artist_name} has {followers} on spotify
    #print = Here is the artwork for {album title}, {album_URL}
    #print = Here are the lyrics for {song_title}: 
    #print = {lyrics}
    pass

preform_menu_selection()
