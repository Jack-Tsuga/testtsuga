from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!abc123aaaaaa</p>"

@app.route("/test")
def hello_world():
   return "<p>test test test</p>"