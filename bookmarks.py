from peewee import *

db = SqliteDatabase('bookmarks.sqlite')

class Bookmarks(Model):
    artist = CharField()
    album_title = CharField()
    song_title = CharField()
    followers = CharField()
    album_art = CharField()
    lyrics = CharField()
    id = None

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id},{self.artist}, {self.album_title}, {self.song_title}, {self.followers}, {self.album_art}, {self.lyrics}'

db.connect()
db.create_tables([Bookmarks])

#deletes all bookmarks
#def delete_bookmarks():
#    Bookmarks.delete().execute()

#creates a new bookmark
def add_new_bookmark(artist, album_title, song_title, followers, album_art, lyrics):
    new_bookmark = Bookmarks(artist = artist, album_title = album_title, song_title = song_title, followers = followers, album_art = album_art, lyrics = lyrics)
    new_bookmark.save()
    print('Your bookmark has been saved!')

#gets total number of bookmarks
def bookmark_count():
    count = Bookmarks.select()
    return count

#searches for bookmark by ID
#TODO test this function once bookmarks can be created
def search_by_id(id):
    rows = Bookmarks.select().where(Bookmarks.id == id)
    return rows

#deletes bookmark by ID
def delete_by_id(id):
    Bookmarks.delete().where(Bookmarks.id == id).execute()
    print('Your bookmark has been deleted')

def get_all_bookmarks():
    bookmarks = Bookmarks.select()

    if bookmarks:
        for bookmark in bookmarks:
            print('\n', bookmark, '\n')
    else:
        print('There are no bookmarks currently saved')

#TODO other ways to search/querie the DB for bookmarks?