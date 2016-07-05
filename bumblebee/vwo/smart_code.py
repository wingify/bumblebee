# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman <tasdik.rahman@wingify.com>
# @http://tasdikrahman.me

import requests

from bumblebee.constants import HEADERS, ACCOUNT_ID


def tracking_code(slack_client, channel):
    """
    Get Smart Code of accounts

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    """
    from bumblebee.helpers.general_helpers import post_to_slack
    url = "https://app.vwo.com/api/v2/accounts/{id}/tracking-code".format(
            id=ACCOUNT_ID
          )

    resp = requests.get(url, headers=HEADERS)

    if resp.status_code == 200:
        data = resp.json()["_data"]  # <dict>
        sync = data["sync"]  # <str>
        async = data["async"]  # <str>
        response = "Tracking code to be put before the *<head>* tags \n" \
                   "*synchronous* \n ```\n{0}\n``` \n\n" \
                   "*asynchronous* \n ```\n{1}\n``` \n".format(
                        sync, async
                    )
    else:
        response = "Invalid query"

    post_to_slack(slack_client, channel, response)
