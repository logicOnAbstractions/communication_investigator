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

def oauth(code_params={}):
    """ makes an authorisation request to strava. format of the rqst:
        client_id: '47498'
        redirect_uri: 'localhost'
        response_type: 'code'
        approval_prompt: 'auto'
        scope: activity: 'read_all,profile:read_all'
        state: [optional - will be forwarded to the redirect URI, so useful if we need to pick on something at that point after auth

        those are all "in query" - which I guess means they should be encoded as url params
    """

    if code_params.keys():
        print("params keys are present in theory")
    else:
        print("no params keys - using defaults")
        code_params = {"client_id":CLIENT_ID, "redirect_uri": 'http://127.0.0.1', "response_type": "code", "approval_prompt": "auto", "scope": "activity:read_all,profile:read_all", "state": "i am the state"}




        oauth_full_url = requests.Request('GET', OAUTH_CODE_ROOT_URL, params=code_params).prepare().url

        print(f"Please visit this URL, review the permissions requested & click Authorize if satisfied:")
        print(f"{oauth_full_url}")
        print(f"you will then be redirected to 127.0.0.1, e.g. localhost, and the URL will contain:")
        print(f"http:/(....)&code=b9d4b3bcd690fa1d3dfb81e4e40024363745caf7&scope(....)")
        code = input("Please enter the alphanumeric code, excluding the termination symbol '&' at the end:")
        print(f"the code entered was {code}. Validating with strava... ")

        # now we need to do a POST

        token_params = {"client_id": 47498, "client_secret":CLIENT_SECRET,"code":code, "grant_type":"authorization_code" }
        TOKEN_POST_URL = requests.post(OAUTH_TOKEN_ROOT_URL, params=token_params)
        print(f"TOKEN: {TOKEN_POST_URL}")


        # basically we need some user input for that to work, e.g. the button click. maybe selenium would be able to do that for us, but in the meantime have to do manually
        # response = requests.get(OAUTH_ROOT_URL, params=params)
        # print(response.status_code)
        # print(oauth_full_url)
        # print(response.text)
