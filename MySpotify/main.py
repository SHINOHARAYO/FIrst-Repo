from dotenv import load_dotenv
import os
from spo import MySpotify, a_scope

def top_ten_songs(sp, name):
    tracks = sp.get_tracks_by_artist(name)
    print ("\nHere is top ten song for " + name +":\n")
    for i, tracks in enumerate(tracks):
        print(f"{i + 1}. {tracks['name']}")
    return

name = input("Enter the name of an Artist: ")

sp = MySpotify(0, a_scope)

top_ten_songs(sp, name)


