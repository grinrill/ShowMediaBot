from flask import Flask, request
import urllib3

app = Flask(__name__)

@app.route('/qq', methods=["GET"])
def qq():
    return "hi"
