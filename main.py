from flask import Flask, request, abort
import os

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

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["T5WVWRdXZpn7WhvddBANP7yMKya92IMb64AD5C7zuZLJXluX5V/ay8EKPR49jJPSMtZ1zb7o/AF07w0D0irUwPYsEylDtmBStL+4FnPbMhtgByrGX/F64YrEtfv901F3Jo3Ua7fUTiUfjHwdjEfNKAdB04t89/1O/w1cDnyilFU="]
LINE_CHANNEL_SECRET = os.environ["673e6242bfa5dec3d43b3eee06859647"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
 # get X-Line-Signature header value　残す
 signature = request.headers['X-Line-Signature']

 # get request body as text　残す
　body = request.get_data(as_text=True)
　app.logger.info("Request body: " + body)

    handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, 
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    # app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)