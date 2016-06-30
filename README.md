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

## Miscelleneous

`flake8` needs to be installed manually for `pep8` conformancy.

    $ pip install flake8
    $ make flake8

## Run it

Install the dependencies

    $ make deps

Running the bot

    $ make run

## LICENSE

All rights Reserved 2016

Wingify Software
