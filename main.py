from flask import Flask, request, abort
# import flask
# from flask import request
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import TextSendMessage
import gunicorn
import os
import logging #48 のapp がおそらくflaskのloggingとして認識されてると思い、標準モジュールの呼び出しを行った

# app = Flask(__name__)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world!"
