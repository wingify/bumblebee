# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman <tasdik.rahman@wingify.com>
# @http://tasdikrahman.me

import requests

from bumblebee.constants import HEADERS, ACCOUNT_ID


def tracking_code():
    """
    Get Smart Code of accounts
    """
    url = "https://app.vwo.com/api/v2/accounts/{id}/tracking-code".format(
            id=ACCOUNT_ID
          )

    resp = requests.get(url, headers=HEADERS)

    if resp.ok:
        return resp
    else:
        return "Invalid query"
