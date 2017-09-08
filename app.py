# encoding: utf-8
import sys

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/YA4Il76UUbHb4YCuk9pWqpcBRgfk8VOFHc+W8FbRy9Vi61I0vC0theYhjYnOrtUxQG6q3sAMSLAGm1ZEATyRsTEnpms+yYykxCXHxC7Tj5u0hlzRHmivk2xNzS7gcO5U6hf8AbebhY7Qf5ju/yaSQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('3a376ac7d336060b079f677c5f3b414c') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value

    p("flag1")
    signature = request.headers['X-Line-Signature']
    p("signature:"+signature);

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    p("Request body: " + body);

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    p("flag2");
    text = event.message.text #message from user
    p("text:"+text);
    p("event.reply_token:"+event.reply_token);
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    
def p(*args):
  print args[0] % (len(args) > 1 and args[1:] or [])
  sys.stdout.flush()    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])