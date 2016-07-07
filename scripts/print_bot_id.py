#!/usr/bin/env python

from bumblebee.constants import SLACK_TOKEN, BOT_NAME

import configparser

from slackclient import SlackClient

config = configparser.ConfigParser()

sc = SlackClient(SLACK_TOKEN)

if __name__ == '__main__':
    api_call = sc.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if user.get('name') == BOT_NAME:
                print('Bot id for ' + user['name'] + 'is : ' + user.get('id'))
    else:
        print('could not find a user named : ' + BOT_NAME)
