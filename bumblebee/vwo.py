# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

import requests

from constants import HEADERS

def get_all_campaigns(slack_client, channel, account_id, limit, offset):
    """
    gets all the campaigns for the particular account_id
    """
    url = "https://app.vwo.com/api/v2/accounts/{id}/campaigns?limit={limit}&offset={offset}".format(
        id=account_id,
        limit=limit,
        offset=offset
    )

    campaign_data = {}

    resp = requests.get(url, headers=HEADERS)

    if resp.status_code == 200:
        data = resp.json()
        campaign_data["num_of_campaigns"] = len(data['_data'])
        # campaign_data["campaign_wise_data"] = []

        # for count, campaign in enumerate(data['_data']):
        #     temp_dict = {}
        #     campaign_data["id"] = campaign["id"]
        #     campaign_data["name"] = campaign["name"]
        #     campaign_data["type"] = campaign["type"]
        #     campaign_data["status"] = campaign["status"]
        #     campaign_data["primaryUrl"] = campaign["status"]
        #     campaign_data["campaign_wise_data"].append(temp_dict)

        response = "Campaign data for the user specified\n"\
                   "Total number of campaigns: {0}".format(
                       campaign_data["num_of_campaigns"]
                   )
    else:
        response = "Invalid query"

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def campaign_status(account_id, campaign_id):
    """Returns the campaign status from the campaign id passed to the bot"""
    pass