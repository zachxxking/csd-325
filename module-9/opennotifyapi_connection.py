# Program: Connection to Open Notify API (Assignment 9.2)
# Authors: Zachariah King
# Date: 3/9/25
# Description: This program uses requests and json to retrieve information
#              from the Open Notify API for the astronauts currently in space.

import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())