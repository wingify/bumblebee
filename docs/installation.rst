Installation
============

You can setup ``bumblebee`` using any of the two methods

Building from source
--------------------

Install the dependencies::

    $ git clone ssh://git@stash.wingify.com:7999/vwo/bumblebee_bot.git
    $ cd bumblebee
    $ virtualenv env              # Create virtual environment
    $ source env/bin/activate     # Change default python to virtual one
    (env)$ make deps

Before running the bot, you have to configure it for your VWO API token and slack API tokens. Assuming that you are in the directory, ``bumblebee``::

    $ cd bumblebee
    $ cp config.ini.example config.ini
    $ cat config.ini
    [slack]
    SLACK_BOT_TOKEN=
    BOT_ID=
    BOT_NAME=

    [vwo]
    VWO_API_TOKEN=
    ACCOUNT_ID=


They are left blank, set to them up to dance with ``bumblebee``

``BOT_ID`` should be retrieved using the script below::

    from slackclient import SlackClient

    BOT_NAME = 'starterbot'  # replace 'starterbot' with the name of your bot name

    slack_client = SlackClient('token')  # replace 'token' with your slack bot token


    if __name__ == "__main__":
        api_call = slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
        else:
            print("could not find bot user with the name " + BOT_NAME)


Place this ``BOT_ID`` in your ``config.ini`` and run the bot::

    (env)$ make run

**NOTE**

Check whether the bot can connect to the ``slack RTM API`` by running::

    $ cd bumblebee
    $ python -m unittest tests.test_slack_api_auth


Dockerfile
----------

A quicker way to get up and running would be to build the ``Dockerfile`` here::

    $ git clone ssh://git@stash.wingify.com:7999/vwo/bumblebee_bot.git
    $ cd bumblebee_bot

Next step would be to get your file ``config.ini``. And place the appropriate tokens.
Get ``BOT_ID`` by running the script above.

Build the image using the ``dockerfile``::

    $ docker build --no-cache=true -t bumblebee .


Run your bot::

    $ docker run -it \
    -e SLACK_BOT_TOKEN="YOUR_SLACK_BOT_TOKEN" \
    -e BOT_ID="YOUR_BOT_ID" \
    -e VWO_API_TOKEN="YOUR_VWO_API_TOKEN" \
    -e ACCOUNT_ID="YOUR_ACCOUNT_ID" \
    -e BOT_NAME="YOUR_BOT_NAME" \
    bumblebee make run

Where you should replace the ``token`` values with yours
