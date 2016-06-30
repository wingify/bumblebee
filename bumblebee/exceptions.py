# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @http://tasdikrahman.me

"""
Custom exceptions for out Bot Bumblebee
"""


class BumblebeeError(Exception):
    """A bumbleBee related error"""

    def __call__(self, *args):
        return self.__class__(*(self.args + args))

BumblebeeException = BumblebeeError


class SettingFileNotFound(BumblebeeError):
    """
    Raised when there is an error related to
    """


class TokensNotSet(BumblebeeError):
    """
    Raised when there the tokens for slack or VWO are not set by the user
    """


class SlackClientErorr(BumblebeeError):
    """
    Raised when there is a problem initializing the slack client object
    """