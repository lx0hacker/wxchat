#!/usr/bin/env python
#-*- coding:utf-8 -*-
from app import app
from flask import request,render_template,make_response
from app.func import tuling,xmlParse,ReceiveMsg,ReceiveTextMsg,ReceiveImageMsg,ReplyTextMsg,ReplyImageMsg
import hashlib

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weixin',methods=['GET','POST'])
def auto_reply():
    if request.method == 'GET':
        token = app.config['TOKEN']
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        data = [timestamp,nonce,token]
        data.sort()
        data = ''.join(data)
        if hashlib.sha1(data.encode('utf-8')).hexdigest() == signature:
            return make_response(echostr)
    else:
        webData = request.stream.read()
        messageClass = xmlParse(webData)
        if isinstance(messageClass,ReceiveMsg) and messageClass.MsgType == 'text':
            toUser = messageClass.ToUserName
            fromUser = messageClass.FromUserName
            code,content = tuling(messageClass.Content)
            reply_message = ReplyTextMsg(toUser,fromUser,content)
            return reply_message.send()
        else:
            print('暂时不处理......')
            return 'success'


