#!/usr/bin/env python 
#-*- coding:utf-8 -*-
import os

class Config(object):
    TOKEN = os.environ.get('TOKEN')
    TULING_URL = 'http://www.tuling123.com/openapi/api'
    APIKEY = os.environ.get('T_APIKEY')
