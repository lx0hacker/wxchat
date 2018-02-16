#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import json
from app import app


def tuling(msg):
    data = {
        "key":app.config['APIKEY'],
        'info':msg
    }
    r = requests.post(app.config['TULING_URL'],data=data)
    content = json.loads(r.text)
    return content['code'],content['text']



