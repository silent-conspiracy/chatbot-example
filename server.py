from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAADQnlo6QEwBAOQ0ZAI8TvZC82nVNW2PCt0sTYdsZBfexG9xIj7NzpnsMpHhZAx155ZAtNQhGHO24ZCf0QQdrC5pHElx6vlYujbmVLqrQZB2q62OReVZBY9hSYv8Mfh7uw2rTMQWpUvBXSkuHo9M4KEYVSxGlEReM13Bs1MDwqdSmgZDZD"
VERIFY_TOKEN = "Weeeee"

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/webhooks', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"


@app.route('/webhooks', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    for entry in data['entry']:
        for message_item in entry['messaging']:
            sender = message_item['sender']['id']
            if message_item.get('message'):
                message = message_item['message']['text']
                reply(sender, message)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
