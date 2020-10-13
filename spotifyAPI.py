#this module is for connecting to the spotify API and managing Authorization
import base64
import datetime
from urllib.parse import urlencode
import os
import pprint

import requests

#you can retreive these from Spotify's developmer page by signing in and starting a new project
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

#Access tokens are deliberately set to expire after a short time, 
 #after which new tokens may be granted by supplying the refresh token originally obtained during the authorization code exchange.
 #The request is sent to the token endpoint of the Spotify Accounts service:

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

    #GET requests for searching for things from the API requires Auth


client = SpotifyAPI(client_id, client_secret)

#tests if preform auth returns true and if acess token is retrieved
#print(client.preform_authorization())
#print(client.access_token)

access_token = client.access_token

        #TEMP USER INPUT VALUE adding test variable here and will repalce this with UI value 
querie_search = 'beyonce'
        #querie type should always be artist
querie_type = 'artist'

headers = {'Authorization': f'Bearer {access_token}'}
endpoint = 'https://api.spotify.com/v1/search'
data = urlencode({'q':f'{querie_search}', 'type':f'{querie_type}'}) #using urlencode to make it a url ready string

lookup_url = f'{endpoint}?{data}'
r = requests.get(lookup_url,headers=headers)
#print(r.json())
followers = r.json()
    
follower_count = followers['total']

print(follower_count)

