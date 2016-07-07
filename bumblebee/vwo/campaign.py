# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman <tasdik.rahman@wingify.com>
# @http://tasdikrahman.me

import requests

from bumblebee.constants import HEADERS, ACCOUNT_ID
from bumblebee.helpers.vwo_helpers import (get_all_campaigns_parser,
                                           get_all_campaigns_printer,
                                           parse_campaign_dict,
                                           print_campaign_data)


def get_all_campaigns(slack_client, channel, limit=15, offset=0):
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
        data = resp.json()["_data"]  # <list>
        campaign_data = get_all_campaigns_parser(data)  # <list>
        response = get_all_campaigns_printer(campaign_data)
    else:
        response = "Invalid query"

    post_to_slack(slack_client, channel, response)


def get_campaign_details(slack_client, channel, campaign_id):
    """
    Returns the campaign status from the campaign id passed to the bot


    :NOTE: BASE URL: https://app.vwo.com/api/v2/accounts/:account_id/campaigns/:campaign_id
           DOCS URL: http://developers.vwo.com/docs/get-details-of-a-specific-campaign

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :param campaign_id: The campaign id whose details the user wants
    """
    from bumblebee.helpers.general_helpers import post_to_slack

    url = "https://app.vwo.com/api/v2/accounts/{id}/campaigns/{campaign_id}".format(
            id=ACCOUNT_ID,
            campaign_id=campaign_id
          )

    campaign_data = {}

    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        data = resp.json()["_data"]
        campaign_data = parse_campaign_dict(data)
        response = print_campaign_data(campaign_data)
        response += "*You can update the status of the campaigns to " \
                    "['stop', 'run', 'pause'] by querying like * \n" \
                    "*update campaign <campaign_id> status to <new_campaign_status> *"
    elif resp.status_code == 404:
        response = "The campaign does not exist!"
    else:
        response = "Invalid query"

    post_to_slack(slack_client, channel, response)


def share_campaign(slack_client, channel, campaign_id):
    """
    Get share link for a specific campaign

    :NOTE: BASE URL: https://app.vwo.com/api/v2/accounts/:account_id/campaigns/:campaign_id/share
           DOCS URL: http://developers.vwo.com/docs/get-share-link-for-a-specific-campaign


    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :param campaign_id: The campaign id whose details the user wants
    """
    from bumblebee.helpers.general_helpers import post_to_slack

    url = "https://app.vwo.com/api/v2/accounts/{id}/campaigns/{cid}/share".format(
                id=ACCOUNT_ID,
                cid=campaign_id
           )

    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        response = "Share link for campaign {no} \n {link}".format(
                        no=campaign_id,
                        link=resp.json()["_data"]["shareLink"]
                    )
    elif resp.status_code == 404:
        response = "The campaign does not exist!"
    else:
        response = "Invalid query"

    post_to_slack(slack_client, channel, response)


def update_campaign_status(slack_client, channel, campaign_id, new_status):
    """
    Update campaign status

    :NOTE: BASE URL: https://app.vwo.com/api/v2/accounts/:account_id/campaigns/status
           DOCS URL: http://developers.vwo.com/docs/update-a-campaign-1

    :param slack_client: SlackClient Object
    :param channel: The channel where the bot needs to post the message
    :param campaign_id: The campaign id whose details the user wants
    :param new_status: The status to which the user wants a campaign to be
                       updated to
    """
    from bumblebee.helpers.general_helpers import post_to_slack

    url = "https://app.vwo.com/api/v2/accounts/{id}/campaigns/status".format(
                id=ACCOUNT_ID
            )

    valid_campaign_status = {
        "run": "RUNNING",
        "stop": "STOPPED",
        "pause": "PAUSED"
    }

    try:
        parsed_status = valid_campaign_status[new_status]
        json_data = {"ids": [campaign_id], "status": parsed_status}
        resp = requests.patch(url, headers=HEADERS, json=json_data)
        if resp.status_code == 200:
            response = "Current status of campaign {id} changed to *{status}*".format(
                            id=campaign_id,
                            status=resp.json()['_data']['status']
                        )
        else:
            response = "Looks like you don't have the required privileges"
    except KeyError:
        response =  "Looks like you entered an invalid status\n" \
                    "valid statuses are : {keys}".format(
                        keys=[key for key in valid_campaign_status.keys()]
                    )

    finally:
        post_to_slack(slack_client, channel, response)
        get_campaign_details(slack_client, channel, campaign_id)
