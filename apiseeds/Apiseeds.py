import requests

class Apiseeds():
    """
    Object to make requests via apiseeds lyrics api https://apiseeds.com/documentation/lyrics
    """

    def __init__(self, api_key):
        # load enviornment variables
        if api_key == None:
            raise Exception("api_key not set")
        self._API_KEY = api_key
        self.API_ROOT = "https://orion.apiseeds.com/api/music/lyric/"
        self.base_params = {
            "apikey": self._API_KEY,
        }

    def call_service(self, artist, track):
        try:
            response = requests.get(
                f"{self.API_ROOT}{artist}/{track}", self.base_params)
            return response
        except Exception as err:
            print(err)


    def get_lyrics(self, artist, track):
        """
        @param string artist: artist to search for
        @param string track: track to search for
        """
        return self.call_service(artist, track)