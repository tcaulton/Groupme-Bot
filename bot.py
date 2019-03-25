
import requests
import time
botId = ''
groupId = ''
token = ''
botName = ''
members = []
def sendmessage(message):
    post_params = {'bot_id': botId, 'text': message}
    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)

def getMembers():
    token = 'b3tfjUbTUueT8X7rItbfcXqC9kiZ1BX5iG5xMSl7'
    request_params = {'token': token}
    response = requests.get('https://api.groupme.com/v3/groups/' + groupId, params=request_params)
    data = response.json()
    for i in data['response']['members']:
        members.append(i['user_id'])
    return members

def alertCheck():
    request_params = {'token': token}
    response = requests.get('https://api.groupme.com/v3/groups/' + groupId, params=request_params)
    data = response.json()
    word = ''
    message = data['response']['messages']['preview']['text']
    for x in message:
        if (x == ' '):
            if (data['response']['messages']['preview']['nickname'] == botName):
                break
            elif (word == 'Tedalert'):
                sendmessage(message)
                break
            elif (word == 'tedalert'):
                sendmessage(message)
                break
        word = word + x
def pingTest():
    request_params = {'token': token, 'limit': 1}
    response_messages = requests.get('https://api.groupme.com/v3/groups/' + groupId + '/messages', params=request_params).json()['response']['messages']
    for message in response_messages:
        if (message['text'] == 'ping'):
            sendmessage('ping1')
            break

def mention():
    getMembers()
while True:
    mention()
    '''
    pingTest()
    alertCheck()
    time.sleep(5)
    '''


