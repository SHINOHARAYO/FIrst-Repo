import sys
import os
import spotipy
import spotipy.util as sp_util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials, SpotifyOauthError
from spotipy.client import SpotifyException
from dotenv import load_dotenv
import base64
from requests import post
import json

a_scope = 'user-library-read playlist-read-private'

class MySpotify:

    Err_Code = 0
    __client_id = ''
    __client_secret=''

    def __init__(self, type=0, scope='', env_id_name='SPOTIPY_CLIENT_ID', env_secret_name='SPOTIPY_CLIENT_SECRET') -> None:
        
        #initialzation
        load_dotenv()
        self.scope = scope
        self.__client_id = os.getenv('SPOTIPY_CLIENT_ID')
        self.__client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')
        
        #get authentication token
        self.__auth_string = self.__client_id + ":" + self.__client_secret
        auth_bytes = self.__auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
        auth_url = "https://accounts.spotify.com/api/token"
        auth_headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        auth_data = {
            "grant_type": "client_credentials"
        }
        auth_result = post(auth_url, headers=auth_headers, data=auth_data)

        #convert auth_token into string
        json_auth_result = json.loads(auth_result.content)
        self.token = {"Authorization": "Bearer " + json_auth_result["access_token"]}

        # authenticaiton phase
        if type == 0:
            # client authentication
            try:
                self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
            except SpotifyOauthError as e:
                self.Err_Code = 0
        
        elif type == 1:
            # user authentication
            # TODO user credentials
            print("TODO")
            pass

        
   