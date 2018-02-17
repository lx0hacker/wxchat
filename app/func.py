#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import json
import time
import xml.etree.ElementTree as ET
from app import app

def xmlParse(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    MsgType = xmlData.find("MsgType").text
    if MsgType == 'text':
        return ReceiveTextMsg(xmlData)
    elif MsgType == 'image':
        return ReceiveImageMsg(xmlData)

    

class ReceiveMsg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text  
    
class ReceiveTextMsg(ReceiveMsg):
    def __init__(self,xmlData):
        ReceiveMsg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")

class ReceiveImageMsg(ReceiveMsg):
    def __init__(self,xmlData):
        ReceiveMsg.__init__(self,xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text



class ReplyMsg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"

class ReplyTextMsg(ReplyMsg):
    def __init__(self,toUserName,fromUserName,content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content.encode('utf-8')
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)

class ReplyImageMsg(ReplyMsg):
    def __init__(self):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)



def tuling(msg):
    data = {
        "key":app.config['APIKEY'],
        'info':msg
    }
    r = requests.post(app.config['TULING_URL'],data=data)
    content = json.loads(r.text)
    return content['code'],content['text']



