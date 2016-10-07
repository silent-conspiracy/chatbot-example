from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAADQnlo6QEwBALiQicnXI8oTDX3gl9siAb9BrjEesU1GyFkIpGOZCrZCztHEuVoPP0jPq4gaI5xMnQkWciTQIQe5FMrSFyXHz8pV41YKAZBN1S3rQZACPqpZCdNKZCwDIvZBZAlJ9MF6MR6QnINmuCpegtY1dCymUsCLugsTPXP0fQZDZD"
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
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
