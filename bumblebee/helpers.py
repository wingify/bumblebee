# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

"""
Has various helper functions defined to help the slack bot reply to a query
"""

from constants import AT_BOT
from vwo import get_all_campaigns


def help(slack_client, channel):
    """Will show every possible interaction with the slack bot"""
    response = "How can I help you?" \
               "\nPossible commands that you can query for:\n" \
               "1) *get_all_campaigns* <account_id>:<int> <limit>:<int> <offset>:<int>"

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def default_resp(slack_client, channel):
    """
    Default response which bumblebee will give if it cannot make out what
    the user is asking for
    """
    response = "Not sure what you meant. Type *@starterbot* *help* for a list of possbile commands"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                command = output['text'].split(AT_BOT)[1].strip().lower()
                channel = output['channel']
                return command, channel
    return None, None


def handle_command(slack_client, command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """

    if "get_all_campaigns" in command:
        command_split_up = command.split()

        split_data = command.split()
        # making key value pairs out of this format
        # Eg: "account_id:243020 limit:25 offset:0"
        temp_dict = {}

        for elem in split_data[1:]:
            k, v = elem.split(":")
            temp_dict[k] = v
        get_all_campaigns(
            slack_client, channel, temp_dict["account_id"], temp_dict["limit"], temp_dict["offset"])

    elif "help" in command:
        help(slack_client, channel)

    else:
        default_resp(slack_client, channel)
