from __future__ import print_function

import json,boto3

def queueManager_handler(event, context):
    messageBody = {
        'action' :  event['action'],
        'username': event['username'],
        'password': event['password']
        }

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Find the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName='TestQueue')

    # access identifiers and attributes
    print("SQS URL = " + queue.url)

    # Create a new message
    response = queue.send_message(MessageBody=json.dumps(messageBody))

    # The response is NOT a resource, but gives you a message ID and MD5
    print("SQS Message ID = " + response.get('MessageId'))
    print("SQS Message MD5 = " + response.get('MD5OfMessageBody'))

    #print("action =" + event['action'])
    #print("username =" + event['username'])
    #print("password =" + event['password'])

    message = 'The following message has been queued in successfully: {}'.format(json.dumps(messageBody))
    
    return message