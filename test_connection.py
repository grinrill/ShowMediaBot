from flask import Flask, request
import urllib3

app = Flask(__name__)

@app.route('/qq')
def qq():
    return "hi"

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0')

#ничего не работает
#АААААААААААААААААААААААААААА