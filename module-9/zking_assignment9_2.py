# Program: Connection to Star Wars API (Assignment 9.2)
# Authors: Zachariah King
# Date: 3/9/25
# Description: This program uses requests and json to retrieve information
#              from the Star Wars API for the second listed character
#              and displays it in a nice formatted fashion.

import requests
import json

response = requests.get("https://swapi.dev/api/people/2/")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
jprint(response.json())