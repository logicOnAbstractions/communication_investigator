"""" .py contenant les tests à effectuer"""

import unittest                         # our test lib
import numpy as np                      # if we want to test numpy arrays
from main import MainProgram
import requests
from utils import *
import os
from utilities.logger import *
from utilities.dao import *

class SomeTests(unittest.TestCase):     # on doit hériter de TestCase

    def __init__(self, *args, **kwargs):
        super(SomeTests, self).__init__(*args, **kwargs)
        self.mainprog_volatile = None

    @classmethod
    def setUpClass(cls):
        """
        this runs only once. Set stuff that's useful for ALL test
        Like common values you want to reuse, loading a text file etc.
        """

        cls.mainprog_permanent = MainProgram(logger=LOG)            # e.g. instantiated once at beginning of test and potentially used by many successive tests

    @classmethod
    def tearDownClass(cls):
        "cleanup after all the tests are done. Like freeing a resources, cleaning a temporary repo etc."
        pass


    def setUp(self):
        """ Runs after EACH test. Here we instantiate a new instance
         each test because we don't want the values modified by a previous test to influence the results of the next one"""
        self.mainprog_volatile = MainProgram(logger=LOG)           # instantiated every single test, so new instances all the time

    def tearDown(self):
        """
        Runs after each test. Similar to class teardown
        """
        self.mainprog_volatile = None

    ################################################ tests

    def test_ping_strava(self):
        """ pings strava.com, checks that response is 200 OK"""
        response = self.mainprog_volatile.ping_strava()
        self.assertTrue(response.status_code == 200)
        LOG.info("Ping strava test successfull.")

    def test_get_auth_code(self):
        """ test that we receive 200 OK if initiate the auth from strava"""
        # code = self.mainprog_volatile.launch_oauth_protocol()
        # self.assertTrue(len(code)==40)          # code is 40 alphanums chars

    def test_get_tokens(self):
        """ tests that we can get a access, refresh token using the procedure    """
        code = self.mainprog_volatile.launch_oauth_protocol()
        tokens = self.mainprog_volatile.get_tokens_from_code(code)
        print(tokens)

    def test_mp_configs(self):
        """ checks configs are loaded properly as expected """
        loaded_configs = self.mainprog_volatile.configs
        self.assertEqual(loaded_configs, DiskDao().get_configs())
        LOG.info(f"Main program configs loaded as expected")


    def test_logger(self):
        """ a few things we test regarding handlers in logger, making sure we don't double-register handlers (and thus double the msgs) """

        test_logger = get_root_logger("test_logger", filename=f"testlogs.log")
        test_logger.info(f"test_logger handlers: {test_logger.handlers} ")



if __name__ == '__main__':

    os.environ["ENV"] = "development"
    os.environ["LOG_LEVEL"] = "INFO"
    LOG = get_root_logger("mylogger", filename=f'log.log')
    LOG.debug(f'logger debug level msg ')
    LOG.info(f'logger info level msg ')
    LOG.warning(f'logger warn level msg ')
    LOG.error(f'logger error level msg ')
    LOG.critical(f'logger critical level msg ')
    unittest.main()