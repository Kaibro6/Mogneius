import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://kaibro6: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@github.com/kaibro6/lasybot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
