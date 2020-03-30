import os
from flask import Flask

# 自分の名称を app という名前でインスタンス化
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

