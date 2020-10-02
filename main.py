""" the investigator:
        * takes a fast & light approach. just write lines of code that directly do something already.
        * but do organize them better (cls, methos, files) better regularly. just not constantly.

    - it initiates a communication with a server (standard http stuff).
    - it then manages the back & forth, keeps track of token/cookies etc.
    - i could make it cmdline interactive. e.g. you would have a list of http replies, arg values etc. & you could discuss, essentially, with the server


    Sample requests to obtain an activity by ID:
        http get "https://www.strava.com/api/v3/activities/{id}?include_all_efforts=" "Authorization: Bearer [[token]]"
    Replacing with our vars here:

        ID = 3427572515
        ACCESS_TOKEN =  a06efe7ae0235b961f1d5d5af6a5ed6202106302            # from /settings/api un "My API application" once logged in valid a few days

        http get f"https://www.strava.com/api/v3/activities/{ID}?include_all_efforts=" "Authorization: Bearer ACCESS_TOKEN"



"""

# no classe, no methods, just code for now

import requests     # lib that manages the back & forth
import json
from engine import *

# list of URLs to test
FIZZ_LOCAL = 'http://192.168.0.1/login.htm'
GOOGLE = ''
ACTIVITY_ID = 3427572515            # strava actvity id to get as test
STRAVA_ROOT_URL = 'https://www.strava.com'
ACTIVITIES_URL = '/activities'
ROOT_ACTIVITIES = f'{STRAVA_ROOT_URL}{ACTIVITIES_URL}'

# - first say hello & start conversation
# headers = {'Accept': 'application/json'}
headers = {}
r = requests.get(STRAVA_ROOT_URL, headers=headers)

print("first some sanity checks to ensure we receive an answer that makes any sense")
print("##################### r.headers #####################")
print(f"response status code: {r.status_code}")

if r.status_code == 200:
    ans = status_200()
    #get my activity
    ID = 3427572515     # this the real id of casual saturday night marathon
    ACCESS_TOKEN = "a06efe7ae0235b961f1d5d5af6a5ed6202106302"  # from /settings/api un "My API application" once logged in valid a few days
    request_url = f'https://www.strava.com/api/v3/activities/{ID}?include_all_efforts=" "Authorization: Bearer {ACCESS_TOKEN}'
    response = requests.get(request_url)
    print(f"status for get activity by id: {response.status_code}")

    print("trying just the ping the api ")
    response_2 = requests.get('https://www.strava.com/')
    print(response_2.status_code)

    # okay let's try Oauth
    oauth = oauth()


else:
    ans = status_others()


print("Great. Now... ")