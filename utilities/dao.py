""" Data access object (DAO). manages getting stuff from the right place (disk, db, other containers, etc.) """
import os
from utils import *
import json
from urllib.parse import urljoin
from utilities.logger import *


class Dao:
    """ super class for accessors (file, nwtk etc.)"""
    def __init__(self):
        self.LOG = get_root_logger(BASE_LOGGER_NAME)


class DiskDao(Dao):
    def __init__(self):
        super().__init__()

    # TODO: wrap in try-catch. Better - decorators to wrap those in try-catch
    @staticmethod
    def get_configs():
        """ returns CLIENT_ID, _SECRET etc. from config file """
        with open(os.path.join(USERDATA_DIR, CONFIGS_FILE), 'r') as file:
            configs = json.load(file)
        return configs

    def get_routes_urls(self):
        """ returns a file containing drescp. of route urls structure in strava"""
        with open(os.path.join(UTILITIES_DIR, URLS_FILE), 'r') as file:
            urls = json.load(file)
        return urls

    def update_access_token(self, token):
        """ takes in a token object as sent by strava in response after auth (or on resfresh token) & updates the user data accordingly."""

        # get configs from source. this is a dict. so we can just update its token key with what we received
        configs = self.get_configs()
        configs["credentials"]["token"] = token

        # update the token:{} dictionary with what we received, we write tot he file in this case
        with open(os.path.join(USERDATA_DIR, CONFIGS_FILE), 'w') as file:
            json.dump(configs, file, sort_keys=True, indent=4)
        # save updates/commit or whatever
        self.LOG.info(f"Update user token values. New tokens: {token}")

class StravaDao(Dao):
    def __init__(self):
        super().__init__()
        self.routes = DiskDao().get_routes_urls()

    # accessor for specific urls, e.g. fully constructed ones without the params/body
    @property
    def home_url(self):
        _ = self.routes
        return _["ROOT_URL"]

    @property
    def oauth_code_url(self):
        _ = self.routes
        url = urljoin(urljoin(_["ROOT_URL"], _["OAUTH_CODE"]), _["AUTHORIZE"])
        return url

    @property
    def oauth_token_url(self):
        _ = self.routes
        return urljoin(urljoin(_["ROOT_URL"], _["OAUTH_CODE"]), _["TOKEN"])

    @property
    def refresh_token_url(self):
        _ = self.routes
        return urljoin(urljoin(_["ROOT_URL"], _["OAUTH_CODE"]), _["TOKEN"])



