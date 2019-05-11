from flask import Flask, request
import urllib3

@app.route('/qq', methods=["GET"])
def qq():
    return "hi"
