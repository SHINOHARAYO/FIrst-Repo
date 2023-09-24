from dotenv import load_dotenv
import os

from spo import MySpotify, a_scope

load_dotenv()

id = os.getenv("SPOTIPY_CLIENT_ID")

print(id)

sp = MySpotify(0, a_scope)
print("Artist: " + sp.get_artist("A$AP")["name"] + "\n"
      "ID: " + sp.get_artist("A$AP")["id"] + "\n")