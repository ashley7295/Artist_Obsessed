import unittest
from unittest import TestCase
from peewee import *

import bookmarks
from bookmarks import Bookmarks



test_db = SqliteDatabase('test_bookmarks.sqlite')
tables = [Bookmarks]

class TestBookmarks(TestCase):

    
    def setup(self):
        test_db.connect()
        test_db.create_tables(tables)

    def teardown(self):
        test_db.drop_tables(tables)
        test_db.close()

    def clear_bookmarks(self):
        bookmarks.delete_bookmarks()

    def setUpCase(self):
        self.clear_bookmarks()

    def add_test_data(self):
        self.clear_bookmarks()

        self.bookmark1 = Bookmarks(artist = 'Beyonce', album_title = 'Lemonade', song_title ='Hold Up', followers='123', album_art="url", lyrics="do re mi")
        self.bookmark2 = Bookmarks(artist = 'Beyonce', album_title = '4', song_title ='Countdown', followers='456', album_art="url2", lyrics="fa so la")

        self.bookmark1.save()
        self.bookmark2.save()

    def test_add_bookmark(self):
        self.add_test_data()
        before_count = bookmarks.bookmark_count()
        bookmark = Bookmarks(artist = 'Paramore', album_title = 'After Laughter', song_title = 'Hard Times', followers='123', album_art='url', lyrics = 'do re mi')
        bookmark.save()
        after_count = bookmarks.bookmark_count()
        self.assertEqual(after_count, before_count + 1 )

    def test_delete_bookmark(self):
        self.add_test_data()
        before_count = bookmarks.bookmark_count()
        bookmarks.delete_by_id(1)
        after_count = bookmarks.bookmark_count()
        self.assertEqual(after_count, before_count - 1) 
    
    def test_get_bookmark_by_id(self):
        self.add_test_data()
        result = bookmarks.search_by_id(self.bookmark1.id)
        self.assertEqual(result, self.bookmark1)

if __name__ == '__main__':
    unittest.main()