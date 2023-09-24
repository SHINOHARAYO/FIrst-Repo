from dotenv import load_dotenv
import os

from spo import MySpotify, a_scope

name = input("Enter the name of an Artist: ")

sp = MySpotify(0, a_scope)
print("Artist: " + sp.get_artist(name)["name"] + "\n"
      "ID: " + sp.get_artist(name)["id"] + "\n")