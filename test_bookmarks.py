import unittest
from unittest import TestCase
from peewee import *

import bookmarks
from bookmarks import Bookmarks

tables = [Bookmarks]

test_db = SqliteDatabase('test_bookmarks.sqlite')

class TestBookmarks(TestCase):

    def setup(self):
        test_db.bind(tables, bind_refs=False, bind_backrefs=False)
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

        self.bookmark1 = Bookmarks(followers='123', album_art="url", lyrics="do re mi")
        self.bookmark2 = Bookmarks(followers='456', album_art="url2", lyrics="fa so la")

        self.bookmark1.save()
        self.bookmark2.save()

    def test_add_bookmark(self):
        self.add_test_data
        bookmark_count = bookmarks.bookmark_count()
        bookmark = Bookmarks(followers='123', album_art='url', lyrics = 'do re mi')
        bookmark.save()
        self.assertEqual(bookmark_count +1, bookmarks.bookmark_count())
    
    def test_get_bookmark_by_id(self):
        self.add_test_data()
        result = bookmarks.bookmark_by_id(self.bookmark1.id)
        self.assertEqual(result, self.bookmark1)

if __name__ == '__main__':
    unittest.main()

