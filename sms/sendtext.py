# Be sure to import the helper gateway class
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from pattern.en import sentiment, polarity, subjectivity, positive
from models import Insms


def getusersearchword(request):

    global newsearchword1, newoption1
    newoption1 = ""
    newsearchword1 = ""

    if (request.method == 'POST'):
        newsearchword1 = request.POST['searchword']
        newoption1 = request.POST['select_option']
    return newsearchword1 , newoption1




def receivedsms(message1):

    message1 = []
    newmessage1 = []

    username = "karanjaeric"
    apikey = "54e6934ca4fb2b2f675fc2534246719efb37389d5341a590d6c3a042f4d83275"

    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)

    # Any gateway errors will be captured by our custom Exception class below,
    # so wrap the call in a try-catch block
    try:
        # Our gateway will return 10 messages at a time back to you, starting with
        # what you currently believe is the lastReceivedId. Specify 0 for the first
        # time you access the gateway, and the ID of the last message we sent you
        # on subsequent results
        lastReceivedId = 38217145;

        while True:
            messages = gateway.fetchMessages(lastReceivedId)

            for message in messages:
                #this is for test purposes
                keyword = message['text'].split()
                message1.append({'from': message['from'], 'to': message['to'], 'date': message['date'], 'text': message['text'],'polarity': polarity(message['text']), 'keyword':keyword[0]})
                obj, created = Insms.objects.get_or_create(sender=message['from'], to=message['to'], date=message['date'],
                                                           text=message['text'], polarity=polarity(message['text']), keyword=keyword[0].lower())
                print keyword[0]
                print created
                lastReceivedId = message['id']
            if len(messages) == 0:
                break


    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while fetching messages: %s' % str(e)
    return (message1)


def smscount(smsCount):
    smsCount2 = len(smsCount)
    return (smsCount2)

def posisms(messages1):
    posisms = 0
    for sms in messages1:
        if sms.polarity > 0:
            posisms +=1
    return (posisms)

def negsms(messages1):
    negsms = 0
    for sms in messages1:
        if sms.polarity < 0:
            negsms +=1
    return (negsms)

def neutsms(messages1):
    neutsms = 0
    for sms in messages1:
        if sms.polarity == 0:
            neutsms +=1
    return (neutsms)
