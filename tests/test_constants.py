# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

"""Tests whether all the constants were set or not"""

import unittest
import os
import configparser

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_FILE = os.path.join(PROJECT_DIR, 'bumblebee', 'config.ini')


class TestingSettingsTokens(unittest.TestCase):

    @unittest.skipIf(not os.path.isfile(SETTINGS_FILE),
                    "You have to create 'config.ini' file in 'bumblebee' project root first!" \
                    "For example configuration, check 'config.ini.example'")
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read(SETTINGS_FILE)

    def test_config_variables(self):
        self.assertIsInstance(self.config.get('slack', 'SLACK_BOT_TOKEN'), str)
        self.assertIsInstance(self.config.get('slack', 'BOT_ID'), str)
        self.assertIsInstance(self.config.get('slack', 'BOT_NAME'), str)
        self.assertIsInstance(self.config.get('vwo', 'VWO_API_TOKEN'), str)
        self.assertIsInstance(self.config.get('vwo', 'ACCOUNT_ID'), str)

    def tearDown(self):
        pass
