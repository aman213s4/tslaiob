#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6299571621:AAED-dip5CMEgT_jbUDTMCO5TBepCS3OiNg")
    API_ID = int(os.environ.get("API_ID", "11907098"))
    API_HASH = os.environ.get("API_HASH", "742e029a552c123ef6c154c5525952bb")
    AUTH_USERS = "6141953122"

