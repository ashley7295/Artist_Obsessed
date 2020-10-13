import requests
from dotenv import load_dotenv
import os

class Apiseeds():
    """
    Object to make requests via apiseeds lyrics api https://apiseeds.com/documentation/lyrics
    """

    def __init__(self):
        # load enviornment variables
        load_dotenv()
        self._API_KEY = os.getenv("apiseeds_api_key")
        self.API_ROOT = "https://orion.apiseeds.com/api/music/lyric/"
        self.base_params = {
            "apikey": self._API_KEY,
        }

    def call_service(self, artist, track):
        response = requests.get(
            f"{self.API_ROOT}{artist}{track}", self.base_params)
        return response.json()

    def get_lyrics(self, artist, track):
        """
        @param string artist: artist to search for
        @param string track: track to search for
        """
        return self.call_service(artist, track)