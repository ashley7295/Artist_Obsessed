

def program_intro_message():
    print('\n WELCOME TO ~ARTIST OBSESSED~ \n')
    print('The program will search for information about an artist and provide thier follower count, album artwork and song lyrics.')
    print('You also can bookmark searches and search from your previously bookmarked searches.')
    print('please select an option below to begin: \n')

def get_artist_name():
    artist_name = input('What is the name of the artist you are searching for?: ')
    return artist_name

def get_album_name():
    album_name = input('What is the name of the album you are looking for?: ')
    return album_name

def get_song_name():
    song_title = input('What is the name of the song you are looking for?: ')
    return song_title

def save_bookmark():
    save_bookmark = input('Do you want to save this as a bookmark? (Y/N): ')
    
    #TODO resolve error where always returning True
    if save_bookmark == 'Y' or 'y':
        return True
    elif save_bookmark == 'N' or 'n': 
        return False
    else:
        print('Please enter a valid Y/N entry.')

def search_by_id():
    ID = int(input('Please enter the ID of the Bookmark you would like to select: '))
    return ID

def print_message(msg):
    return print(msg)


def print_menu():
    print(' 1: Start Search querie')
    print(' 2: Display all Bookmarks')
    print(' 3: Search for a bookmark by ID')
    print(' 4: Delete a Bookmark by ID')
    print(' 5: Quit')

    user_selection = int(input('Please enter the number of the menu item you would like to select: '))

    if user_selection in range (1, 6):
        return user_selection
    else:
        print('Please enter a valid number between 1 & 5')