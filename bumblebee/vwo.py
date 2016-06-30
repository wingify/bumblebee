# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

import requests

from bumblebee.constants import HEADERS, ACCOUNT_ID


def get_all_campaigns(slack_client, channel, limit=25, offset=0):
    """
    gets all the campaigns for the particular account_id

    :NOTE: BASE URL: https://app.vwo.com/api/v2/accounts/:account_id/campaigns
           DOCS URL: http://developers.vwo.com/docs/get-the-campaigns-of-an-account

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :param limit: limit the number of campaigns to be returned
    :param offset: Offset where campaign should be fetched from
    :returns: Help message
    """
    from bumblebee.helpers.general_helpers import post_to_slack
    url = "https://app.vwo.com/api/v2/accounts/{id}/campaigns?limit={limit}&offset={offset}".format(
        id=ACCOUNT_ID,
        limit=limit,
        offset=offset
    )

    campaign_data = {}

    resp = requests.get(url, headers=HEADERS)

    if resp.status_code == 200:
        data = resp.json()
        campaign_data["num_of_campaigns"] = len(data["_data"])
        all_campaign_data = data["_data"]  # type<list>

        response = "Getting all Campaign data for the user specified\n"\
                   "Total number of campaigns: {0}".format(
                       campaign_data["num_of_campaigns"]
                   )
    else:
        response = "Invalid query"

    post_to_slack(slack_client, channel, response)


def campaign_status(account_id, campaign_id):
    """
    Returns the campaign status from the campaign id passed to the bot
    """
    pass
