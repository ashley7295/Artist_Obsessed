import unittest
from unittest import TestCase
from unittest.mock import patch, call
import os

from spotifyAPI import *

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

spotify = SpotifyAPI(client_id, client_secret)

class TestSpotifyAPI(TestCase):
    
    test_response = test_response = {
        "time": {
            "updated": "Oct 20, 2020 15:03:00 UTC",
            "updatedISO": "2020-10-20T15:03:00+00:00",
            "updateduk": "Oct 20, 2020 at 16:03 BST"
        },
        "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName": "Bitcoin",
        "bpi": {
            "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "11,906.8495",
            "description": "United States Dollar",
            "rate_float": 11906.8495
            },
            "GBP": {
            "code": "GBP",
            "symbol": "&pound;",
            "rate": "9,180.5382",
            "description": "British Pound Sterling",
            "rate_float": 9180.5382
            },
            "EUR": {
            "code": "EUR",
            "symbol": "&euro;",
            "rate": "10,073.3614",
            "description": "Euro",
            "rate_float": 10073.3614
            }
        }
    }
    
    def test_preform_authorization(self):
        test = True
        auth_preformed = spotify.preform_authorization()
        self.assertTrue(test, auth_preformed)


    @patch('spotifyAPI.search_artist_data', side_effect = [test_response])
    def test_search_artist_data(self, mock_querie):
        mock_querie = 'beyonce'
        response = spotify.search_artist_data(mock_querie)
        self.assertEqual(response, self.test_response)

if __name__ == '__main__':
    unittest.main()