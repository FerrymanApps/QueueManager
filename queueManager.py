from __future__ import print_function

import json

def queueManager_handler(event, context):
    messageBody = {
        'action' :  event['action'],
        'username': event['username'],
        'password': event['password']
        }

    print("action =" + event['action'])
    print("username =" + event['username'])
    print("password =" + event['password'])

    message = 'The following message has been queued in successfully: {}'.format(json.dumps(messageBody))
    
    return message