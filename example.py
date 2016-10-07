from wit import Wit

def send(request, response):
    print "Sending to user...", response[text]

def my_action(request):
    print "Received from user... ", request[text]

actions = {
    'send': send,
    'my_action': my_action,
}

access_token = "USBWIGGGHRS2VETEL2HWGFXCTKH52N5D"

client=Wit(access_token=access_token, actions=actions)


