#!/usr/bin/env python

import os
import configparser

from slackclient import SlackClient

config = configparser.ConfigParser()

FILE_NAME = os.path.abspath(__file__)
DIRNAME = os.path.dirname(FILE_NAME)
SETTINGS_FILE = os.path.join(DIRNAME, 'bumblebee', 'config.ini')
BOT_NAME = 'starterbot'

config.read(SETTINGS_FILE)
sc = SlackClient(config.get('slack', 'SLACK_BOT_TOKEN'))

if __name__ == '__main__':
    api_call = sc.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if user.get('name') == BOT_NAME:
                print('Bot id for ' + user['name'] + 'is : ' + user.get('id'))
    else:
        print('could not find a user named : ' + BOT_NAME)
