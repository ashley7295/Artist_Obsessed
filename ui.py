def get_string(message):
    while True:
        response = input(message)
        if response is not None:
            return response

def get_int(message):
    while True:
        try:
            response = int(input(message))
            return response
        except ValueError:
            print('Please enter a number ')

def get_int_in_range(message, min, max):
    while True:
        response = get_int(message)
        if response in range (min, max + 1):
            return response
        else:
            print(f'Please enter a valid number between {min} & {max}')
        
def program_intro_message():
    print('\n WELCOME TO ~ARTIST OBSESSED~ \n')
    print('The program will search for information about an artist and provide thier follower count, album artwork and song lyrics.')
    print('You also can bookmark searches and search from your previously bookmarked searches.')
    print('please select an option below to begin: \n')

def get_artist_name():
    message = 'What is the name of the artist you are searching for?: '
    artist_name = get_string(message)
    return artist_name

def get_album_name():
    message = 'What is the name of the album you are looking for?: '
    album_name = get_string(message)
    return album_name

def get_song_name():
    message = 'What is the name of the song you are looking for?: '
    song_title = get_string(message)
    return song_title

def save_bookmark():
    save_bookmark = input('Do you want to save this as a bookmark? (Y/N): ')
    
    if save_bookmark == 'Y' or 'y':
        return True
    elif save_bookmark == 'N' or 'n': 
        return False
    else:
        print('Please enter a valid Y/N entry.')

def search_by_id():
    message = 'Please enter the ID of the Bookmark you would like to select: '
    id = get_int(message)
    return id

def print_message(msg):
    return print(msg)


def print_menu():
    print(' 1: Start Search querie')
    print(' 2: Display all Bookmarks')
    print(' 3: Search for a bookmark by ID')
    print(' 4: Delete a Bookmark by ID')
    print(' 5: Quit')

    message = 'Please enter the number of the menu item you would like to select: '
    user_selection = get_int_in_range(message, 1, 6)
    return user_selection
