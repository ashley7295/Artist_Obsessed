import requests
import os
import logging

class Musix():
    """
    Object to make requests via MusixMatch API
    """

    def __init__(self, api_key):
        # load enviornment variables
        if api_key == None:
            raise Exception("api_key not set")
        self._API_KEY = api_key
        self.MUSIC_MATCH_API_ROOT = "https://api.musixmatch.com/ws/1.1/"
        self.base_params = {
            "apikey": self._API_KEY,
        }

    def call_service(self, endpoint, params):
        query = self.base_params.copy()
        query.update(params)
        try:
            response = requests.get(f"{self.MUSIC_MATCH_API_ROOT}{endpoint}", query)
            return response
        except requests.exceptions.RequestException as exception:
            # TODO: what sould be done with this exception
            logging.info(exception)


class Track(Musix):
    def __init__(self, api_key):
        Musix.__init__(self, api_key)

    def album_track_get(self, album_id, page=0, page_size=20, has_lyrics=True):
        """
        Get tracklist by album id
        Can optionally pass in page, page_size modify results

        @param string album_id: album id
        @param int page: Define the page number for paginated results (default 0)
        @param int page_size: Define the page size for paginated results.Range is 1 to 100 (default 20)
        @param bool has_lyrics: filter results by lyric existance (default True)
        """
        endpoint = 'album.get.track'
        params = {
            "album_id": album_id,
            "f_has_lyrics": has_lyrics,
            "page": page,
            "page_size": page_size
        }
        return self.call_service(endpoint, params)

    def matcher_track_get(self, artist, track, has_lyrics=True):
        """
        Search for track by artist name and track name

        @param string artist: artist name
        @param string track: track name
        @param bool has_lyrics: When set, filter only contents with lyrics (default True)
        """
        endpoint = "matcher.track.get"
        params = {
            "q_artist": artist,
            "q_track": track,
            "f_has_lyrics": has_lyrics
        }
        return self.call_service(endpoint, params)

    def track_get(self, track_id):
        """
        Get track by track id

        @param string track_id: track id to search for
        """
        endpoint = 'track.get'
        params = {
            "track_id": track_id,
        }
        return self.call_service(endpoint, params)

    def track_search(self, track_name=None, artist_name=None, lyrics=None, artist_id=None, genre_id=None, has_lyrics=True, sort_artist=None, sort_track=None, page=0, page_size=20):
        """
        Searches for a track by name

        @param string track_name: Track name to search for
        @param string artist_name: Artist name to search for
        @param string lyrics: Any word in the lyrics to search for
        @param artist_id: Artist id to filter results by
        @param int genre_id: music genre to filter results by
        @param bool has_lyrics: When set, filter only contents with lyrics (default True)
        @param string sort_artist: Sort by popularity index for artists (asc|desc)
        @param string sort_track: Sort by popularity index for tracks (asc|desc)
        @param int page: Define the page number for paginated results (default 0)
        @param int page_size: Define the page size for paginated results.Range is 1 to 100 (default 20)
        @return requests.Response.json():
        """
        endpoint = 'track.search'
        params = {
            "q_track": track_name,
            "q_artist": artist_name,
            "q_lyrics": lyrics,
            "f_artist_id": artist_id,
            "f_music_genre_id": genre_id,
            "f_has_lyrics": has_lyrics,
            "s_artist_rating": sort_artist,
            "s_track_rating": sort_track,
            "page": page,
            "page_size": page_size
        }
        # remove unset values
        filtered_params = {key: value for (
            key, value) in params.items() if value is not None}

        return self.call_service(endpoint, filtered_params)

    def chart_tracks_get(self, page=0, page_size=20, country="us", has_lyrics=True):
        """
        Gets tracks by popularity using contry code. Can optionally
        pass in page, page_size and country code to modify results

        @param integer page: Define the page number for paginated results
        @param integer page_size: Define the page size for paginated results.Range is 1 to 100.
        @param string country: A valid ISO 3166 country code
        @param bool has_lyrics: filter results by lyric existance (default True)

        @return requests.Response.json():
        @raise ValueError: When no JSON object could be decoded.
        """
        endpoint = 'chart.tracks.get'
        if (page_size < 1 or page_size > 100):
            print("page_size must be between 0 and 100")
            return False
        # TODO validate country codes
        params = {
            "country": country,
            "page": page,
            "page_size": page_size,
            "f_has_lyrics": has_lyrics
        }
        return self.call_service(endpoint, params)


class Artist(Musix):
    def __init__(self, api_key):
        Musix.__init__(self, api_key)

    def artist_related_get(self, artist_id, page=0, page_size=20):
        """
        @param artist_id: The musiXmatch artist id
        @param integer page: Define the page number for paginated results
        @param integer page_size: Define the page size for paginated results.Range is 1 to 100.
        """
        endpoint = "artist.related.get"
        params = {
            "artist_id": artist_id,
            "page": page,
            "page_size": page_size
        }
        return self.call_service(endpoint, params)

    def artist_search(self, song_artist, artist_id, page=0, page_size=20):
        """
        @param string song_artist: song artist to search for
        @param artist_id: The musiXmatch artist id to fiter by
        @param integer page: Define the page number for paginated results
        @param integer page_size: Define the page size for paginated results.Range is 1 to 100.
        """
        endpoint = "artist.search"
        params = {
            "q_artist": song_artist,
            "artist_id": artist_id,
            "page": page,
            "page_size": page_size
        }
        return self.call_service(endpoint, params)

    def artist_get(self, artist_id):
        """
        @param artist_id: The musiXmatch artist id
        """
        endpoint = "artist.get"
        params = {
            "artist_id": artist_id
        }
        return self.call_service(endpoint, params)

    def chart_artists_get(self, page=0, page_size=20, country="us"):
        """
        @param integer page: Define the page number for paginated results
        @param integer page_size: Define the page size for paginated results.Range is 1 to 100.
        @param string country: A valid ISO 3166 country code
        """
        endpoint = "chart.artist.get"
        params = {
            "page": page,
            "page_size": page_size,
            "country": country
        }
        return self.call_service(endpoint, params)


class Album(Musix):
    def __init__(self, api_key):
        Musix.__init__(self, api_key)

    def album_get(self, album_id):
        """
        @param album_id: The musiXmatch album id
        """
        endpoint = "album.get"
        params = {
            "album_id": album_id
        }
        return self.call_service(endpoint, params)

    def artist_album_get(self, artist_id, release_date=None, album_name=None, page=0, page_size=20):
        """
        @param string artist_id: The musiXmatch artist id
        @param string releaes_date: Sort by release date (asc|desc)
        @param string album_name: Group by album name
        @param integer page: Define the page number for paginated results
        @param integer page_size: Define the page size for paginated results.Range is 1 to 100.
        """
        endpoint = "artist.album.get"
        params = {
            "artist_id": artist_id,
            "s_release_date": release_date,
            "g_album_name": album_name,
            "page": page,
            "page_size": page_size
        }
        filtered_params = {key: value for (
            key, value) in params.items() if value is not None}
        return self.call_service(endpoint, filtered_params)


class Lyrics(Musix):
    def __init__(self, api_key):
        Musix.__init__(self, api_key)

    def matcher_lyrics_get(self, artist_name, track_name):
        """
        Search for lyrics by artist name and track name

        @param string artist_name: artist name
        @param string track_name: track name
        """
        endpoint = "matcher.lyrics.get"
        params = {
            "q_artist": artist_name,
            "q_track": track_name,
        }
        return self.call_service(endpoint, params)

    def track_lyrics_get(self, track_id):
        """
        @param string track_id: The musiXmatch track id
        """
        endpoint = "lyrics.get"
        params = {
            "track_id": track_id
        }
        return self.call_service(endpoint, params)
