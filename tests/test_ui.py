from unittest import TestCase
from unittest.mock import patch

import ui

class TestUi(TestCase):
    @patch('builtins.input', side_effect=['1', 'fake_response'])
    def test_get_string(self, mock):
        message = 'message'
        response = ui.get_string(message)
        self.assertTrue(response, 'fake_response')

    @patch('builtins.input', side_effect=['fake_response', '1'])
    def test_get_int(self, mock):
        message = 'message'
        response = ui.get_int(message)
        self.assertTrue(response, 1)

    @patch('builtins.input', side_effect=['fake_response', '0', '6', '5'])
    def test_get_int_in_range(self, mock):
        message = 'message'
        response = ui.get_int_in_range(message, 1, 5)
        self.assertTrue(response, 5)
    
    def test_print_message(self):
        message = 'Hello!'
        response = ui.print_message(message)
        self.assertEqual(response, None)

    @patch("builtins.input", side_effect=["5678"])
    def test_search_by_id(self, mock):
        response = ui.search_by_id()
        self.assertEqual(response, 5678)

    @patch("builtins.input", side_effect=["y"])
    def test_save_bookmark_yes(self, mock):
        response = ui.save_bookmark()
        self.assertTrue(response)

    @patch("builtins.input", side_effect=["n"])
    def test_save_bookmark_no(self, mock):
        response = ui.save_bookmark()
        self.assertFalse(response)

    @patch("builtins.input", side_effect=["Selena Gomez"])
    def test_get_artist_name(self, mock):
        response = ui.get_artist_name()
        self.assertEqual(response, "Selena Gomez")

    @patch("builtins.input", side_effect=["Rare"])
    def test_get_album_name(self, mock):
        response = ui.get_album_name()
        self.assertEqual(response, "Rare")

    @patch("builtins.input", side_effect=["Dance Again"])
    def test_get_song_name(self, mock):
        response = ui.get_song_name()
        self.assertEqual(response, "Dance Again")


if __name__ == '__main__':
    unittest.main()
