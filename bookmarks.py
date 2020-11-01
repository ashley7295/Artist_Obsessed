from peewee import *

db = SqliteDatabase('bookmarks.sqlite')

#a bookmark is created with the search parameters and the search results for the user
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
        return f'ID:{self.id}, {self.artist}, {self.album_title}, {self.song_title}, {self.followers}, {self.album_art}, {self.lyrics}'

db.connect()
db.create_tables([Bookmarks])

#deletes all bookmarks
def delete_bookmarks():
    Bookmarks.delete().execute()

#creates a new bookmark
def add_new_bookmark(artist, album_title, song_title, followers, album_art, lyrics):
    new_bookmark = Bookmarks(artist = artist, album_title = album_title, song_title = song_title, followers = followers, album_art = album_art, lyrics = lyrics)
    new_bookmark.save()
    print('Your bookmark has been saved!')

#gets total number of bookmarks
def bookmark_count():
    count = Bookmarks.select().count()
    return count

#searches for bookmark by ID, returns NONE if ID is not in DB
def search_by_id(ID):
    rows = Bookmarks.get_or_none(id = ID)
    if rows is not None:
        return rows
    else:
        return None


#deletes bookmark by ID, returns NONE if ID is not in DB
def delete_by_id(ID):
    rows = Bookmarks.get_or_none(id = ID)

    if rows == None:
        return None
    else:
        delete_bookmark = Bookmarks.delete().where(Bookmarks.id == ID).execute()
        return delete_bookmark
        
#Gets and displays all the bookmarks in the DB
def get_all_bookmarks():
    bookmarks = Bookmarks.select()

    if bookmarks:
        for bookmark in bookmarks:
            print('\n', bookmark, '\n')
    else:
        print('There are no bookmarks currently saved')
