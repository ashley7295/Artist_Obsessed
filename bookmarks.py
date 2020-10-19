from peewee import *

db = SqliteDatabase('bookmarks.sqlite')

class Bookmarks(Model):
    followers = CharField()
    albumArt = CharField()
    lyrics = CharField()
    id = None

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}, {self.followers}, {self.albumArt}, {self.lyrics}'

db.connect()
db.create_tables([Bookmarks])

#deletes all bookmarks
def delete_bookmarks():
    Bookmarks.delete().execute()

#gets total number of bookmarks
def bookmark_count():
    count = Bookmarks.select()

    return count

#searches for bookmark by ID
#TODO test this function once bookmarks can be created
def bookmark_by_id(id):
    rows = Bookmarks.select().where(Bookmarks.id == id)

    return rows

#deletes bookmark by ID
def delete_bookmark_by_id(id):
    Bookmarks.delete().where(Bookmarks.id == id).execute()
    print('Your bookmark has been deleted')

#TODO other ways to search/querie the DB for bookmarks?