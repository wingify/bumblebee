## Bumblebee

Bumblebee is `slackRTM` powered slack bot written in python

Is currently deployed over at https://wingify-test.slack.com/
and is Invitation invite only for now. Although you can join the slack channel with your wingify email.

## Installation

Install the dependencies

    $ git clone ssh://git@stash.wingify.com:7999/vwo/bumblebee_bot.git
    $ cd bumblebee
    $ virtualenv env              # Create virtual environment
    $ source env/bin/activate     # Change default python to virtual one
    (env)$ make deps

Before running the bot, you have to configure it for your VWO API token and slack API tokens. Assuming that you are in the directory, `bumblebee`

```sh
$ cp config.ini.example config.ini
$ cat config.ini
[slack]
SLACK_BOT_TOKEN=
BOT_ID=
BOT_NAME=

[vwo]
VWO_API_TOKEN=
ACCOUNT_ID=
```

They are left blank, set to them up to dance with `bumblebee`

Running the bot

    (env)$ make run

## Dockerfile

A quicker way to get up and running would be to build the `Dockerfile` here.

```sh
$ git clone ssh://git@stash.wingify.com:7999/vwo/bumblebee_bot.git
$ cd bumblebee_bot
$ docker build --no-cache=true -t bumblebee .
```

Next step would be to get your file `config.ini`. And place the appropriate tokens, to get your bot ID

`$ docker run -it bumblebee make bot_id`

Run your bot,

```
$ docker run -it \
-e SLACK_BOT_TOKEN="YOUR_SLACK_BOT_TOKEN" \
-e BOT_ID="YOUR_BOT_ID" \
-e VWO_API_TOKEN="YOUR_VWO_API_TOKEN" \
-e ACCOUNT_ID="YOUR_ACCOUNT_ID" \
-e BOT_NAME="YOUR_BOT_NAME" \
bumblebee make run
```

Where you should replace the `token` values with yours

## Miscelleneous

`flake8` needs to be installed manually for `pep8` conformancy.

    $ pip install flake8
    $ make flake8

**NOTE**: For getting your `BOT_ID`, run. This is assuming that you have
already specified the required tokens in the `bumblebee/config.ini` file


```sh
$ make bot_id
```

## Links

- [VWO Docs](http://developers.vwo.com/docs/introduction/)
- [Token Generation](https://app.vwo.com/#/developers/tokens/)


## LICENSE

All rights Reserved 2016

Author: [Tasdik Rahman](http://tasdikrahman.me/) [(@tasdikrahman)](https://twitter.com/tasdikrahman/)

[Wingify Software LTD](http://wingify.com/)