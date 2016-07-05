# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman <tasdik.rahman@wingify.com>
# @http://tasdikrahman.me

"""
Stiches everything together to make Bumblebee work
"""

import time

from slackclient import SlackClient

from bumblebee.constants import SLACK_TOKEN, READ_WEBSOCKET_DELAY
from bumblebee.exceptions import SlackClientErorr
from bumblebee.helpers.general_helpers import parse_slack_output, handle_command


# instantiate Slack client
try:
    slack_client = SlackClient(SLACK_TOKEN)
except Exception:
    raise SlackClientErorr("Invalid SLACK API TOKEN")


def runner():
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(slack_client, command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
