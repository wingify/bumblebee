# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

"""
Has various helper functions defined to help the slack bot reply to a query
"""

from bumblebee.constants import AT_BOT
from bumblebee.vwo import get_all_campaigns, get_campaign_details


def post_to_slack(slack_client, channel, response):
    """
    Helper to post to appropriate slack channel

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :param response: message to be posted to a slack channel by the bot
    :returns: Default message when bot cannot parse user input
    """
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def help(slack_client, channel):
    """
    Will show every possible interaction with the slack bot

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :returns: Help message
    """
    response = "How can I help you?" \
               "\nPossible commands that you can query for:\n" \
               "1) *get all campaigns* : shows the last 15 campaign data \n" \
               "2) *get campaign details <campaign id>* : shows all data for a specific campaign\n"
    post_to_slack(slack_client, channel, response)


def default_resp(slack_client, channel):
    """
    Default response which bumblebee will give if it cannot make out what
    the user is asking for

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :returns: Default message when bot cannot parse user input
    """
    response = "Not sure what you meant"
    post_to_slack(slack_client, channel, response)


def parse_slack_output(slack_rtm_output):
    """
    The Slack Real Time Messaging API is an events firehose.
    this parsing function returns None unless a message is
    directed at the Bot, based on its ID.

    :param slack_rtm_output: string recieved from slack RTM API
    :returns command: user query
    :returns channel: channel where the bot has to return the response
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

    :param slack_client: SlackClient Object
    :returns command: user query
    :param channel: The channel where the bot needs to post the message
    """

    if "get all campaigns" in command:
        # split_data = command.split()
        # making key value pairs out of this format
        # Eg: "account_id:243020 limit:25 offset:0"
        # temp_dict = {}

        # for elem in split_data[1:]:
        #     k, v = elem.split(":")
        #     temp_dict[k] = v

        # limit = temp_dict.get("limit", 25)
        # offset = temp_dict.get("offset", 0)
        get_all_campaigns(slack_client, channel)

    elif "get campaign details" in command:
            campaign_id = command.split()[-1]
            get_campaign_details(slack_client, channel, campaign_id)

    elif "help" in command:
        help(slack_client, channel)

    else:
        default_resp(slack_client, channel)
        help(slack_client, channel)
