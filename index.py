from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!abc123aaaaaa</p><a href='test'>TEST</a>"

@app.route("/test")
def test():
   return "<p>test test test</p>"