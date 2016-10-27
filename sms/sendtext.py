# Be sure to import the helper gateway class
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Specify your login credentials
username = 'MyUsername'
apikey = 'MyApikey'

# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)

# Any gateway errors will be captured by our custom Exception class below,
# so wrap the call in a try-catch block
try:
    # Our gateway will return 10 messages at a time back to you, starting with
    # what you currently believe is the lastReceivedId. Specify 0 for the first
    # time you access the gateway, and the ID of the last message we sent you
    # on subsequent results
    lastReceivedId = 0;

    while True:
        messages = gateway.fetchMessages(lastReceivedId)

        for message in messages:
            print 'from=%s;to=%s;date=%s;text=%s;linkId=%s;' % (message['from'],
                                                                message['to'],
                                                                message['date'],
                                                                message['text'],
                                                                message['linKId']
                                                                )
            lastReceivedId = message['id']
        if len(messages) == 0:
            break


except AfricasTalkingGatewayException, e:
    print 'Encountered an error while fetching messages: %s' % str(e)
