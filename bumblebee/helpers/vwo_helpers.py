# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman <tasdik.rahman@wingify.com>
# @http://tasdikrahman.me

"""
Helper functions for vwo API output parsing
"""

import time


def parse_campaign_dict(campaign_dict):
    """
    Parses the JSON data for a particular campaign ID

    :param campaign_dict: <dict> Campaign specific JSON data
    :returns: A <dict> which is printed by 'print_campaign_data()'
    """
    temp_dict = {}
    # temp_dict["clickCount"] = campaign_dict["clickCount"]
    # convert epoch time to easy readable format
    temp_dict["createdOn"] = time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.localtime(campaign_dict["createdOn"])
                            )
    temp_dict["name"] = campaign_dict["name"]
    temp_dict["status"] = campaign_dict["status"]
    temp_dict["type"] = campaign_dict["type"]
    temp_dict["primaryUrl"] = campaign_dict["primaryUrl"]
    temp_dict["id"] = campaign_dict["id"]

    return temp_dict


def print_campaign_data(parsed_campaign_dict):
    """
    Prints the parsed campaign dict

    :param parsed_campaing_dict: The parsed campaign data returned by
                                 parse_campaign_dict
    :returns: A formatted string to be posted to the slack channel
    """
    response = "*Campaign id :{id}*\n"\
               "Name: {name}\n"\
               "Type: {type}\n"\
               "Status: {status}\n"\
               "Created on: {created_on}\n\n"\
               "URL: {url}\n".format(
                   id=parsed_campaign_dict["id"],
                   name=parsed_campaign_dict["name"],
                   type=parsed_campaign_dict["type"],
                   status=parsed_campaign_dict["status"],
                   created_on=parsed_campaign_dict["createdOn"],
                   url=parsed_campaign_dict["primaryUrl"]
                )
    return response


def get_all_campaigns_parser(_data):
    """
    Parser for the JSON data

    :param _data: A listThe raw JSON data returned back from the API
    :returns: A <dict> which is then parsed to print the parsed data
    """
    campaign_data = []
    for data in _data:  # _data => <list>
        # data => <dict>
        temp_dict = parse_campaign_dict(data)  # data => <dict>
        campaign_data.append(temp_dict)

    return campaign_data


def get_all_campaigns_printer(campaign_data):
    """
    Parses the campaign_data dict to pretty print it in the slack channel

    :param campaign_data: <list> The dict to be pretty printed in the slack channel
    :returns response: <str> which should be printed
    """
    response = "Getting all Campaign data for the user specified\n"\
               "*Total campaigns: {0}* \n".format(len(campaign_data))
    for campaign in campaign_data:
        response += print_campaign_data(campaign)

    response += "\nIf you want details for a *specific campaign*, type\n" \
                "​*campaign details <campaign id>*​"

    return response
