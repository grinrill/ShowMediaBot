from flask import Flask, request
import urllib3

app = Flask(__name__)

@app.route('/qq')
def qq():
    return "hi"

@app.route('/yandex_0e7083bb3ed93679.html')
def qq():
    return """<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>Verification: 0e7083bb3ed93679</body>
</html>"""

#if __name__ == '__main__':
#    app.run(ssl_context=('/home/grinrill/certs/grinrill.ml/fullchain.pem', '/home/grinrill/certs/grinrill.ml/privkey.pem'), host='0.0.0.0')
if __name__ == '__main__':
	app.run(host='0.0.0.0', port="8080")