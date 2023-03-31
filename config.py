#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6299571621:AAHk0oGTA-OuYTBCup_gUMeYEXl1OIs65DM")
    API_ID = int(os.environ.get("API_ID", "24632110"))
    API_HASH = os.environ.get("API_HASH", "ffb85e2ade96e600c1b03377dc67a8b3")
    AUTH_USERS = "6141953122"

