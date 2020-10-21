#this module is for connecting to the spotify API and managing Authorization
import base64
import datetime
from urllib.parse import urlencode
import os
import pprint

import requests

#you can retreive these from Spotify's developer page by signing in and starting a new project
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

#sets up auth tokens and expirations, client_id and client_secret, and token URL
class SpotifyAPI():
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token' 
    #url HTTP request: Request Body Parameters(grant_type needs to be set to client_credentials)

    #init, establishes the cliet ID and client Secret required by the spotify API
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret


    #From spotify API documentation:
    # Access tokens are deliberately set to expire after a short time, 
    # after which new tokens may be granted by supplying the refresh token originally obtained during the authorization code exchange.
    # The request is sent to the token endpoint of the Spotify Accounts service:


    #POST request is required
    #The header of this post request must contain authorization
    def get_client_credentials(self):
        #returns a base64 encoded string for the auth header
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception ("You must set a client_id and client_secret") #these are required params
        client_credentials = f'{client_id}:{client_secret}'
        client_credentials_b64 = base64.b64encode(client_credentials.encode())
        return client_credentials_b64.decode()

    #gets client credentials (client_id & client_secret) and created the Header Parameter
    def get_token_headers(self):
        client_credentials_b64 = self.get_client_credentials()
        return{'Authorization': f'Basic {client_credentials_b64}'}

    def get_token_data(self):
        return{'grant_type': 'client_credentials'}

    #preforms auth but does not retrieve the access token
    def preform_authorization(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()

        r = requests.post(token_url,data=token_data,headers=token_headers)

        if r.status_code not in range(200, 299):
            print(r.status_code)
            raise Exception('Could not Authenticate')
        
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] #seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    #preform_authorization does not get the access token, only checks to see if it exists or hasnt expired
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()

        if expires < now:
            self.preform_authorization()
            return self.get_access_token()
        elif token == None:
            self.preform_authorization()
            return self.get_access_token()
        return token


    #GET requests for searching for things from the API. requires Auth.
    def search_artist_data(self, query):
        querie_type = 'artist' #querie type will always be artist for purposes of this program
        access_token = self.get_access_token()

        headers = {'Authorization': f'Bearer {access_token}'}
        endpoint = 'https://api.spotify.com/v1/search'
        data = {'q':query,'type':querie_type} #using urlencode to make it a url ready string
        
        lookup_url = f'{endpoint}'
        r = requests.get(lookup_url,headers=headers, params = data)
        followers = r.json()
        
        return followers

    def get_follower_count(self, followers):
        follower_count = followers['artists']['items']
        for i in follower_count:
            followers = i['followers']['total']
            follower_string = f'This artist has {followers:,} followers.' #f string formats the big numbers with commas
            follower_list = []
            follower_list.append(follower_string)

            if len(follower_list) == 1: #needs to only grab the first result in the artist "items"
                for i in follower_list: #grabs the only item in the list and returns it so it does not return as a list item
                    return i

    
spotify = SpotifyAPI(client_id, client_secret)
        
data = spotify.search_artist_data('beyonce')
followers = spotify.get_follower_count(data)
print(followers)
