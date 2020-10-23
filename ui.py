


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
    save_bookmark = input('Do you want to save this as a bookmark?: (Y/N) ')
    
    if save_bookmark == 'Y' or 'y':
        return True

def search_by_id():
    ID = int(input('Please enter the ID of the Bookmark you would like to select: '))
    return ID

def print_message(msg):
    return print(msg)

def print_menu():
    print(' 1: Display all Bookmarks')
    print(' 2: Start Search querie')
    print(' 3: Search for a bookmark by ID')
    print(' 4: Delete a Bookmark by ID')
    print(' 5: Quit')

    user_selection = int(input('Please enter the number of the menu item you would like to select: '))

    if user_selection in range (1, 6):
        return user_selection
    else:
        print('Please enter a valid number between 1 & 5')