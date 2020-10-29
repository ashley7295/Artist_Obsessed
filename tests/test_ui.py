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
