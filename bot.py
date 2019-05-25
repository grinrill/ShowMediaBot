
from flask import Flask, request
import telepot
import urllib3

message_id = None
chennel_id = -1001349637964
proxy_url = "http://80.240.25.63:1080"
#forward_from_message_id_err = False
#telepot.api._pools = {
#    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
#}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
print(11)
secret = "769641442:AAFvjT0DjFDWiArc4Yb657KoQck6zuZCgpE"
bot = telepot.Bot(secret)
#bot.setWebhook("https://grinrill.ml:8443/{}".format(secret), max_connections=10)
print(2)
app = Flask(__name__)
print(3)
#app.debug = True


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    print(4)
    update = request.get_json()
    if "message" in update:
        try:
            if  update["message"]["forward_from_message_id"] == message_id:
                return "200"
        except Exception as e:
            pass
        

        text = update["message"]["text"]
        message_id = update["message"]["message_id"]
        chat_id = update["message"]["chat"]["id"]
        print('q1')
        try:
            bot.sendMessage(chennel_id, "Not {}!!!".format(text))
            bot.forwardMessage(chennel_id, chat_id, message_id, True)
            bot.forwardMessage(chat_id, chat_id, message_id, True)
        except Exception as e:
            print(e)
        
        print('q1')
        #bot.sendMessage(chat_id, "Не {}!!!".format(text))
        #bot.sendMessage(chat_id, "Не {}!!!".format(text))
        #bot.forwardMessage(chennel_id, chat_id, message_id, disable_notification=True)
        #bot.sendMessage(chennel_id, "Не {}!!!".format(text))
    return "200"

if __name__ == '__main__':
    app.run(ssl_context=('/home/grinrill/certs/grinrill.ml/fullchain.pem', '/home/grinrill/certs/grinrill.ml/privkey.pem'), host='0.0.0.0', port="8443")