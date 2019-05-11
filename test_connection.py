from flask import Flask, request
import urllib3

app = Flask(__name__)

@app.route('/qq', methods=["GET"])
def qq():
    return "hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#ничего не работает
#АААААААААААААААААААААААААААА