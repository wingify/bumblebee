# -*- coding: utf-8 -*-
# @Author: tasdikrahman
# @http://tasdikrahman.me

"""
Stiches everything together to make Bumblebee work
"""

import os
import time
import configparser

from slackclient import SlackClient

from constants import (SLACK_TOKEN, BOT_ID, VWO_API_TOKEN,
                       AT_BOT, READ_WEBSOCKET_DELAY)
from exceptions import SlackClientErorr
from helpers import (help, default_resp, parse_slack_output,
                     handle_command)


# instantiate Slack client
try:
    slack_client = SlackClient(SLACK_TOKEN)
except Exception:
    raise SlackClientErorr("Invalid SLACK API TOKEN")


if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(slack_client, command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
