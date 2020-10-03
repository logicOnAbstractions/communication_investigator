""" Data access object (DAO). manages getting stuff from the right place (disk, db, other containers, etc.) """
import os
from utils import *
import json
from urllib.parse import urljoin


class Dao:
    """ super class for accessors (file, nwtk etc.)"""
    def __init__(self):
        pass


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

    @staticmethod
    def get_routes_urls():
        """ returns a file containing drescp. of route urls structure in strava"""
        with open(os.path.join(UTILITIES_DIR, URLS_FILE), 'r') as file:
            urls = json.load(file)
        return urls


class StravaDao(Dao):
    def __init__(self):
        super().__init__()
        self.routes = DiskDao.get_routes_urls()

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





