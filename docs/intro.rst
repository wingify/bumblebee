Introduction
============

What is it
----------

Bumblebee is ``slackRTM`` powered slack bot written in python

Is currently deployed over at `https://wingify-test.slack.com/ <https://wingify-test.slack.com/>`_
and is Invitation invite only for now. Although you can join the slack channel with your wingify email.

Usage
-----

After you have deployed your bot. And it's up and running on your slack channel.
You can currently query for the given commands to the bot for your particular ``vwo`` account ID

Each command should be prefixed with the chosen name of your bot.

.. note::

    Example command for help

    ``@starterbot: help``

    Where starterbot would be the name of the bot

``help``
    shows the list of commands which can be given to the bot

``​all campaigns``
    shows the last 15 campaign data

``campaign details <campaign_id>``
    shows all data for a specific campaign

``update campaign <campaign_id> status to <new_campaign_status>``
    updates a campaign status to user specified

``share campaign <campaign_id>``
    Provides a link of the campaign to be shared

``tracking code``
    The tracking code to be installed in your websites