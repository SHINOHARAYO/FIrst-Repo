import sys
import os
import spotipy
import spotipy.util as sp_util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials, SpotifyOauthError
from spotipy.client import SpotifyException
from dotenv import load_dotenv
import base64
from requests import post, get
import json

a_scope = 'user-library-read 、getlist-read-private'

class MySpotify:

    #-------/Public Variables/-------#
    """
    Error code:
        0 No Error
        1 Client Authentication Fail
        2 User Authentication Fail(Incorrect UserID or else)
        10 No Search Result Match

    """
    Err_Code = 0
    scope = ''
    access_token = {}
    #-------/----------------/-------# 


    #-------/Private Variables/-------#
    __client_id = ''
    __client_secret=''
    __auth_string=''
    #-------/-----------------/-------#



    def __init__(self, type=0, scope='', env_id_name='SPOTIPY_CLIENT_ID', env_secret_name='SPOTIPY_CLIENT_SECRET') -> None:
        
        #initialzation
        load_dotenv()
        self.scope = scope
        self.__client_id = os.getenv('SPOTIPY_CLIENT_ID')
        self.__client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')
        
        #get authentication token
        self.__auth_string = self.__client_id + ':' + self.__client_secret
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

        #getting auth tokens
        auth_result = post(auth_url, headers=auth_headers, data=auth_data)

        #convert auth_token into string
        json_auth_result = json.loads(auth_result.content)
        self.access_token = {"Authorization": "Bearer " + json_auth_result["access_token"]}

        # authenticaiton phase
        if type == 0:
            # client authentication
            try:
                self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
            except SpotifyOauthError as e:
                self.Err_Code = 1
        
        elif type == 1:
            # user authentication
            # TODO user credentials
            print("TODO")
            pass
    
    def get_artist_id(self, artist_name):
        query = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"

        search_result = get(query, headers=self.access_token)
        json_result = json.loads(search_result.content)["artists"]["items"]

        # if no result
        if len(json_result) == 0:
            self.Err_Code = 10
            self.err_handler()
            return None 

        return json_result[0]["id"]
    
    def get_tracks_by_artist(self, artist_name):
        artist_id = self.get_artist_id(artist_name)
        query = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
        search_result = get(query, headers=self.access_token)
        json_result = json.loads(search_result.content)["tracks"]
        
        # if no result
        if len(json_result) == 0:
            self.Err_Code = 10
            self.err_handler()
            return None 

        return json_result
    


    def err_handler(self) -> None:
        """
        Error Handler for MySpotify

        Error code:
            0 No Error

            1 Client Authentication Fail

            2 User Authentication Fail(Incorrect UserID or else)

            10 No Search Result Match

        Currently, this will not raise error.
        """        
        if self.Err_Code == 0:
            return
        elif self.Err_Code == 1:
            print("Client Authentication Fail")
            sys.exit(1)
        elif self.Err_Code == 10:
            print ("No Search Result Match")
            sys.exit(10)
        
   