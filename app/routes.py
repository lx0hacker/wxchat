#!/usr/bin/env python
#-*- coding:utf-8 -*-
from app import app
from flask import request,render_template,make_response
from app.func import tuling,xmlParse,ReceiveMsg,ReveiveTextMsg,ReceiveImageMsg,ReplyTextMsg,ReplyImageMsg
import hashlib

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weixin',methods=['GET','POST'])
def auto_reply():
    #code,text = tuling('厦门天气')
    #return render_template('index.html',weather=text)
    if request.method == 'GET':
        token = 'wzwwx1992'
        signature = request.args.get('signature','')
        timestamp = request.args.get('timestamp','')
        nonce = request.args.get('nonce','')
        echostr = request.args.get('echostr','')
        data = [timestamp,nonce,token].sort()
        data = ''.join(data)
        if hashlib.sha1(data).hexdigest() == signature:
            return make_response(echostr)
    else:
        webData = request.stream.read()
        messageClass = xmlParse(webData)
        if isinstance(messageClass,ReceiveMsg) and messageClass.MsgType == 'text':
            toUser = messageClass.ToUserName
            fromUser = messageClass.FromUserName
            content = tuling(messageClass.Content)
            reply_message = ReplyTextMsg(toUser,fromUser,content)
            return reply_message.send()
        else:
            print('暂时不处理......')
            return 'success'


