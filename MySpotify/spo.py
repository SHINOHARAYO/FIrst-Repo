import sys
import os
import spotipy
import spotipy.util as sp_util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials, SpotifyOauthError
from spotipy.client import SpotifyException

scope = 'user-library-read playlist-read-private'

def auth_client():
    '''
    From env credentials to authenticate Spotify Web API.
    '''
    try:
        client_credentials = SpotifyClientCredentials()

        spo = spotipy.Spotify(client_credentials_manager=client_credentials)
        return spo
    except SpotifyOauthError as e:
        print('NO API credentials! FUCK YOU!')
        sys.exit(1)

def auth_user():
    usrName = input("\nGIVE ME YOUR FUCKING USERNAME:")

    try:
        usrToken = sp_util.prompt_for_user_token(usrName, scope=scope)

        spo = spotipy.Spotify(auth=usrToken)
        return usrName, spo
    except SpotifyException as e:
        print('NO API credentials! FUCK YOU!')
        sys.exit(1)
    except SpotifyOauthError as e:
        uri = os.environ.get('SPOTIPY_REDIRECT_URI')
        if uri is not None:
            print("fuck you".format(uri))
        else:
            sys.exit(1)
