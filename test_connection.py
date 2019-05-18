from flask import Flask, request
import urllib3

app = Flask(__name__)

@app.route('/qq')
def qq():
    return "hi"

if __name__ == '__main__':
    app.run(ssl_context=('/home/grinrill/certs/grinrill.ml/fullchain.pem', '/home/grinrill/certs/grinrill.ml/privkey.pem'), host='0.0.0.0')
#if __name__ == '__main__':
#	app.run(host='0.0.0.0')