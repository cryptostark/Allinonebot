#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5735888887:AAFlYUmXJ8eIdMt3O68neXcOGkYkYWzwMR4")
    API_ID = int(os.environ.get("API_ID", "1654363"))
    API_HASH = os.environ.get("API_HASH", "26b911420edb5ceb8f370f21f5eb2684")
    AUTH_USERS = "435946586"

