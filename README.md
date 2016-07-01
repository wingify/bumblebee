## Bumblebee

Bumblebee is `slackRTM` powered slack bot written in python

Is currently deployed over at https://wingify-test.slack.com/
and is Invitation invite only for now. Although you can join the slack channel with you wingify email.

## Configuration

Set the API Tokens for the bot in the file

```sh
$ cd bumblebee && cp config.ini.example config.ini
$ cat config.ini
[slack]
SLACK_BOT_TOKEN=
BOT_ID=

[vwo]
VWO_API_TOKEN=
ACCOUNT_ID=
```

## Links

- [VWO Docs](http://developers.vwo.com/docs/introduction/)
- [Token Generation](https://app.vwo.com/#/developers/tokens/)

## Installation

Install the dependencies

    $ git clone ssh://git@stash.wingify.com:7999/vwo/bumblebee_bot.git
    $ cd bumblebee
    $ virtualenv env              # Create virtual environment
    $ source env/bin/activate     # Change default python to virtual one
    (env)$ make deps

Running the bot

    (env)$ make run

## Miscelleneous

`flake8` needs to be installed manually for `pep8` conformancy.

    $ pip install flake8
    $ make flake8


## LICENSE

All rights Reserved 2016

Author: [Tasdik Rahman](http://tasdikrahman.me/) [(@tasdikrahman)](https://twitter.com/tasdikrahman/)

[Wingify Software LTD](http://wingify.com/)
