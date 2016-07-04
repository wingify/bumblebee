# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

"""
Contains the initialization of all the configuration settings for the slack bot
"""

import os

from bumblebee.exceptions import (SettingFileNotFound, TokensNotSet)


READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

FILE_NAME = os.path.abspath(__file__)
DIRNAME = os.path.dirname(FILE_NAME)
SETTINGS_FILE = os.path.join(DIRNAME, 'config.ini')

"""check whether the file 'config.ini' exists or not"""
if os.path.isfile(SETTINGS_FILE):
    import configparser
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE)

    try:
        SLACK_TOKEN = config.get('slack', 'SLACK_BOT_TOKEN')
        BOT_ID = config.get('slack', 'BOT_ID')
        VWO_API_TOKEN = config.get('vwo', 'VWO_API_TOKEN')
        ACCOUNT_ID = config.get('vwo', 'ACCOUNT_ID')
        HEADERS = {'content-type': 'application/json', 'token': VWO_API_TOKEN}
    except Exception:
        raise TokensNotSet("Set the appropriate tokens in 'config.ini'")

else:
     # If the config.ini file does not exist
    response = "The file 'config.ini' was not set!"\
               "\nLooking for set environment variables"
    # raise SettingFileNotFound(response)
    SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
    BOT_ID = os.environ.get('BOT_ID')
    VWO_API_TOKEN = os.environ.get('VWO_API_TOKEN')
    ACCOUNT_ID = os.environ.get('ACCOUNT_ID')
    HEADERS = {'content-type': 'application/json', 'token': VWO_API_TOKEN}

AT_BOT = "<@" + BOT_ID + ">:"
