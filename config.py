#!/usr/bin/env python 
#-*- coding:utf-8 -*-
import os

class Config(object):
    TOKEN = os.environ.get('TOKEN')
    TULING_URL = 'http://www.tuling123.com/openapi/api'
    APIKEY = os.environ.get('T_APIKEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")or\
                           'mysql+pymysql://test:qwe123@127.0.0.1/cve'
