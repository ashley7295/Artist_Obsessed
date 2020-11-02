import unittest
from unittest import TestCase
from unittest.mock import patch, call
import os

from spotifyAPI import *

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

spotify = SpotifyAPI(client_id, client_secret)

class TestSpotifyAPI(TestCase):
    
    #test response for follower count
    test_response = {
   "artists":{
      "href":"https://api.spotify.com/v1/search?query=beyonce&type=artist&offset=0&limit=20",
      "items":[
         {
            "followers":{
               "href":"None",
               "total":24802657
         }},
            ]}}
    
    #test process auth
    def test_process_authorization(self):
        test = {'access_token': 1234, 'expires_in': 0}
        auth_process = spotify.process_authorization(test)
        self.assertTrue(auth_process)

    #test that a follower count is being retrieved
    def test_get_follower_count(self):
        test_follower_count = f'{24802657:,}'
        response = spotify.get_follower_count(self.test_response)
        self.assertEqual(test_follower_count, response)


if __name__ == '__main__':
    unittest.main()