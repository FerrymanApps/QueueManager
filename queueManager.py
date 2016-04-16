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

    print("####################################")
    print("Begin Writing SQS Message")
    print("####################################")

    # Create a new message
    response = queue.send_message(MessageBody=json.dumps(messageBody))

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response)
    print(response['ResponseMetadata']['HTTPStatusCode'])

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("The message was successfully written!")
    else:
        print("The message was not written and needs to be sent to Error Handler")

    print("SQS Message ID = " + response.get('MessageId'))
    print("SQS Message MD5 = " + response.get('MD5OfMessageBody'))

    print("####################################")
    print("Finish Writing SQS Message")
    print("####################################")

    print("####################################")
    print("Begin Reading SQS Message")
    print("####################################")

    # Read a message
    message = queue.receive_messages(AttributeNames=['All'])
    print(message[0])
    print("Message ID = " + message[0].message_id)
    print("Message Body = " + message[0].body)
    print(message[0].attributes)
    print("Message TimeStamp = " + message[0].attributes['SentTimestamp'])

    ### Question for Dana: How do you maintain popping out messages in order.
    ### How to pop out the functions into a package.
    ### Error Handling?
    ### How to call other web services?

    print("####################################")
    print("Finish Reading SQS Message")
    print("####################################")

    print("####################################")
    print("Begin Deleting SQS Message")
    print("####################################")

    response_del = message[0].delete()

    print(response_del)
    print(response_del['ResponseMetadata']['HTTPStatusCode'])
    
    if response_del['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("The message was successfully deleted!")
    else:
        print("The message was not deleted and needs to be sent to Error Handler")


    print("####################################")
    print("Finish Deleting SQS Message")
    print("####################################")

    message = 'The following message has been processed in successfully: {}'.format(json.dumps(messageBody))

    return message