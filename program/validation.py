""" classes that validates credentials etc. """
import time
from utilities.dao import *
import requests
import json
from utilities.logger import *
from utils import *

class TokenManager:
    """ keeps a reference to the token when the program is up & running. is in charge of checking for expiraiton etc...
        when we need to access the API
    """
    def __init__(self, dao=DiskDao()):
        self.dao = dao
        self.tokens = self.dao.get_configs()
        self.refresh_threshold = 3000           # how many seconds before expiration we will automatically ask for a new access token with the rfresh one
        self.LOG = get_root_logger(BASE_LOGGER_NAME)

    # TODO: some decorator system to wrap those calls in try/except somewhat like we didi with dekko
    def validate_credentials(self):
        """ given credentials, checks that the data is valid. calls for a refresh token if needed """
        now = time.time()
        if self.expires_at - now <= self.refresh_threshold:         # ask for a new token with refresh token
            refresh = self.refresh_access_token()
            return refresh
        else:
            return True

    # TODO: decorator err mngmt
    def refresh_access_token(self):
        """
        updates the access token in the user configs
        :return: True if successfull, false if not
        """
        url = StravaDao().refresh_token_url
        response = requests.post(url, params=self.refresh_token_params)
        if response.status_code == 200:
            tokens = json.loads(response.content)
            self.dao.update_access_token(tokens)
            return True
        else:
            self.LOG.info(f"Failed to refresh token. Strava API response: {response.content}")
            return False

    @property
    def expires_at(self):
        return self.tokens["credentials"]["token"]["expires_at"]

    @property
    def refresh_token_params(self):
        """ returns properly formatted diction. to make a refresh token call to strava """
        params = {"client_id": self.client_id, "client_secret": self.client_secret,
                        "grant_type": "refresh_token", "refresh_token":self.refresh_token}
        return params
    @property
    def client_id(self):
        return self.tokens["credentials"]["CLIENT_ID"]
    @property
    def client_secret(self):
        return self.tokens["credentials"]["CLIENT_SECRET"]
    @property
    def refresh_token(self):
        return self.tokens["credentials"]["token"]["refresh_token"]
