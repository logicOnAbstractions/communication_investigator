"""" .py contenant les tests à effectuer"""

import unittest                         # our test lib
import numpy as np                      # if we want to test numpy arrays
from main import MainProgram
import requests
from utils import *
import os
from logger import get_root_logger

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

        cls.mainprog_permanent = MainProgram(LOGGER=LOG)            # e.g. instantiated once at beginning of test and potentially used by many successive tests

    @classmethod
    def tearDownClass(cls):
        "cleanup after all the tests are done. Like freeing a resources, cleaning a temporary repo etc."
        pass


    def setUp(self):
        """ Runs after EACH test. Here we instantiate a new instance
         each test because we don't want the values modified by a previous test to influence the results of the next one"""
        self.mainprog_volatile = MainProgram(LOGGER=LOG)           # instantiated every single test, so new instances all the time

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