# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman <tasdik.rahman@wingify.com>
# @http://tasdikrahman.me

"""
Has various helper functions defined to help the slack bot reply to a query
"""

import re

from bumblebee.constants import AT_BOT
from bumblebee.vwo.campaign import (get_all_campaigns,
                                    get_campaign_details,
                                    share_campaign,
                                    update_campaign_status)
from bumblebee.vwo.smart_code import tracking_code


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
               "1) *all campaigns* : shows the last 15 campaign data \n" \
               "2) *campaign details <campaign_id>* : shows all data for a specific campaign\n" \
               "3) *update campaign <campaign_id> status to <new_campaign_status> *\n" \
               "4) *share campaign <campaign_id>* : Provides a link of the campaign to be shared \n" \
               "5) *tracking code* : The tracking code to be installed in your websites"
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

    if "all campaigns" in command:
        get_all_campaigns(slack_client, channel)

    elif "campaign details" in command:
        campaign_id = command.split()[-1]
        try:
            temp = int(campaign_id)
            get_campaign_details(slack_client, channel, campaign_id)
        except ValueError:
            response = "Looks like you didn't mention the campaign number!\n" \
                       "The query should look like! \n" \
                       "*campaign details <campaign_id>* : shows all data for a specific campaign"
            post_to_slack(slack_client, channel, response)

    elif "share campaign" in command:
        campaign_id = command.split()[-1]
        try:
            temp = int(campaign_id)
            share_campaign(slack_client, channel, campaign_id)
        except ValueError:
            response = "Looks like you didn't mention the campaign number!\n" \
                       "The query should look like! \n" \
                       "*share campaign <campaign_id>* : Provides a link of the campaign to be shared "
            post_to_slack(slack_client, channel, response)

    elif "tracking code" in command:
        response = tracking_code()
        data = response.json()["_data"]
        if isinstance(data, dict):
            sync = data["sync"]  # <str>
            async = data["async"]  # <str>
            response = "Tracking code to be put before the *<head>* tags \n" \
                       "*synchronous* \n ```\n{0}\n``` \n\n" \
                       "*asynchronous* \n ```\n{1}\n``` \n".format(
                            sync, async
                        )
        else:
            response = data
        post_to_slack(slack_client, channel, response)

    elif "update campaign" in command:
        new_status = command.split()[-1]
        try:
            campaign_id = int(re.search(r'\d+', command).group())
            update_campaign_status(slack_client, channel, campaign_id, new_status)
        except AttributeError:
            response = "Looks like you didn't mention the campaign number!\n" \
                       "The query should look like! \n" \
                       "*update campaign <campaign_id> status to <new_campaign_status> "
            post_to_slack(slack_client, channel, response)

    elif "help" in command:
        help(slack_client, channel)

    else:
        default_resp(slack_client, channel)
        help(slack_client, channel)
