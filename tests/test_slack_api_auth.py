# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

import unittest
import os
import configparser

from slackclient import SlackClient

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_FILE = os.path.join(PROJECT_DIR, 'bumblebee', 'config.ini')


class TestSLackAuth(unittest.TestCase):

    @unittest.skipIf(not os.path.isfile(SETTINGS_FILE),
                    "You have to create 'config.ini' file in 'bumblebee' project root first!" \
                    "For example configuration, check 'config.ini.example'")
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read(SETTINGS_FILE)
        self.slackclient = SlackClient(self.config.get('slack', 'SLACK_BOT_TOKEN'))

    def test_api(self):
        self.assertTrue(self.slackclient.api_call('auth.test')['ok'])

    def test_slack_auth(self):
        self.assertTrue(self.slackclient.api_call('auth.test')['ok'])

    def tearDown(self):
        pass
