# Import the helper gateway class
from mwananchi.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


def sms_responses(number, response):
    # Specify your login credentials
    username = "SAMMIENJIHIA"
    apikey = "9898e481449e39a6051b3d87e07f4de171bedc93a046dd166c0dad2d0d9b6bdc"

    to = number

    # And of course we want our recipients to know what we really do
    message = response

    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)

    try:

        results = gateway.sendMessage(to, message)

        for recipient in results:
            # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)
