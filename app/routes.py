#!/usr/bin/env python
#-*- coding:utf-8 -*-
from app import app
from flask import request,render_template
from app.tuling import tuling 

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/weixin',methods=['GET','POST'])
def auto_reply():
    code,text = tuling('厦门天气')
    return "<h1>"+text+"</h1>"