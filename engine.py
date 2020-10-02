""" defines stuff to do when some things happen. kind of common methods """
import requests

OAUTH_CODE_ROOT_URL = "https://www.strava.com/oauth/authorize"
OAUTH_TOKEN_ROOT_URL = "https://www.strava.com/oauth/token"
CLIENT_ID = 47498
CLIENT_SECRET = "082737c890f03f2547f847b7635dcc4527a52d2a"
# CLIENT_SECRET = "082737c890f03f2547f847b7635dcc4527a52d2az"         # false one, to test


def status_200():
    return "OK!"

def status_others():
    print("Not OK. Exiting.... ")
    exit(0)
