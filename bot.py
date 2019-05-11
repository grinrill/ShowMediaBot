
from flask import Flask, request
import telepot
import urllib3

message_id = None
chennel_id = -1001349637964
proxy_url = "http://158.130.53.36:8080"
#telepot.api._pools = {
#    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
#}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
print(11)
secret = "769641442:AAHnJbvl0sxsVl-pENmls7FpsVxRhkEttGQ"
bot = telepot.Bot(secret)
bot.setWebhook("https://130.193.50.33/{}".format(secret), max_connections=10)
print(2)
app = Flask(__name__)
print(3)
#app.debug = True


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    print(4)
    update = request.get_json()
    if "message" in update:
        if  update["message"]["forward_from_message_id"] == message_id:
            return "OK"
        text = update["message"]["text"]
        message_id = update["message"]["message_id"]
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chennel_id, "Не {}!!!".format(text))
        bot.forwardMessage(chennel_id, chat_id, message_id, True)
        bot.forwardMessage(chat_id, chat_id, message_id, True)
        #bot.sendMessage(chat_id, "Не {}!!!".format(text))
        #bot.sendMessage(chat_id, "Не {}!!!".format(text))
        #bot.forwardMessage(chennel_id, chat_id, message_id, disable_notification=True)
        #bot.sendMessage(chennel_id, "Не {}!!!".format(text))
    return "OK"

if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0')