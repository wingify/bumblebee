# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

"""
Helper functions for vwo API output parsing
"""

import time


def get_all_campaigns_parser(_data):
    """
    Parser for the JSON data

    :param _data: A listThe raw JSON data returned back from the API
    :returns: A <dict> which is then parsed to print the parsed data
    """
    campaign_data = []
    for data in _data:  # _data => <list>
        # data => <dict>
        temp_dict = {}
        temp_dict["clickCount"] = data["clickCount"]
        # convert epoch time to easy readable format
        temp_dict["createdOn"] = time.strftime('%Y-%m-%d %H:%M:%S',
                                            time.localtime(data["createdOn"])
                                )
        temp_dict["name"] = data["name"]
        temp_dict["status"] = data["status"]
        temp_dict["type"] = data["type"]
        temp_dict["primaryUrl"] = data["primaryUrl"]
        temp_dict["id"] = data["id"]
        campaign_data.append(temp_dict)

    return campaign_data


def get_all_campaigns_printer(campaign_data):
    """
    Parses the campaign_data dict to pretty print it in the slack channel

    :param campaign_data: <list> The dict to be pretty printed in the slack channel
    :returns response: <str> which should be printed
    """
    response = "Getting all Campaign data for the user specified\n"\
               "Total campaigns: {0}\n".format(len(campaign_data))
    for campaign in campaign_data:
        response += "*Campaign id :{id}*\n"\
                   "Name: {name}\n"\
                   "Type: {type}\n"\
                   "Status: {status}\n"\
                   "Created on: {created_on}\n\n"\
                   "URL: {url}\n".format(
                       id=campaign["id"],
                       name=campaign["name"],
                       type=campaign["type"],
                       status=campaign["status"],
                       created_on=campaign["createdOn"],
                       url=campaign["primaryUrl"]
                )

    return response
