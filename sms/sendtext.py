# Be sure to import the helper gateway class
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from pattern.en import sentiment, polarity, subjectivity, positive
from models import Insms
from subscribe.models import Subscribers
from sequence import sequence_match_ratio
from sms_reponse import sms_responses
from django.contrib.auth.models import User



def getusersearchword(request):

    global newsearchword1, newoption1
    newoption1 = ""
    newsearchword1 = ""

    if (request.method == 'POST'):
        newsearchword1 = request.POST['searchword']
        newoption1 = request.POST['select_option']
    return newsearchword1 , newoption1




def receivedsms():

    username = "karanjaeric"
    apikey = "6f19ed4200003a5255a5379062651e177a8cdf3ba09cdef8d7f258bf0a52ee70"

    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)

    # Any gateway errors will be captured by our custom Exception class below,
    # so wrap the call in a try-catch block
    try:
        # Our gateway will return 10 messages at a time back to you, starting with
        # what you currently believe is the lastReceivedId. Specify 0 for the first
        # time you access the gateway, and the ID of the last message we sent you
        # on subsequent results
        ms_id = Insms.objects.values_list('msg_number', flat=True).distinct().last()
        lastReceivedId = ms_id;

        while True:
            messages = gateway.fetchMessages(lastReceivedId)

            if messages:
                usernames = User.objects.all()

                for message in messages:
                    keywords = message['text'].split()

                    # remember to check whether a message is a subscribe message or a normal text message
                    # the msg_type_status of a subscribe msg is false while that of a normal msg is true
                    if len(keywords) == 0: # blank message
                        continue
                    elif len(keywords) == 1: # subscribe message. Holds the username of user to subscribe to
                        # get the keywords and username
                        # for every user, compare their names with that of the received message
                        for username in usernames:
                            keyword1 = keywords[0]

                            ratio1 = sequence_match_ratio(keyword1, username.username)
                            # if the keyword at index 0 and the user's username has a sequence matching ratio of 0.7
                            # or greater then that means that the subscriber wants to subscribe to that usernames
                            #  channel
                            print ("The match ratio in the subscribe message is {}".format(ratio1))
                            if ratio1 >= 1:
                                # check for duplicate message id's
                                if Insms.objects.filter(msg_number=message['id'], keyword=username, msg_type_status=False):
                                    print("Msg Type= subscribe msg This message already exists in our database")
                                else:
                                    # save the received message first. the keyword of this message
                                    # will be the username of the person who's this message is intended for
                                    new_msg = Insms(sender=message['from'],
                                                    to=message['to'],
                                                    date=message['date'],
                                                    text=message['text'],
                                                    polarity=polarity(message['text']),
                                                    keyword=username,
                                                    msg_number=message['id'],
                                                    msg_read_status=True,
                                                    msg_type_status=False)
                                    new_msg.save()
                                    # create an instance of the subscriber
                                    # this is the point you check whether if there's already such kind of subscription
                                    if Subscribers.objects.filter(mobile_number=message['from'], subscribed_topic=username):
                                        print ("This subscription already exists")
                                        response = "You are already subscribed to {} channel. " \
                                                   "You can send a message to this channel starting with the word {} " \
                                                   "followed by your message".format(username, username)
                                        sms_responses(message['from'], response)
                                        # Send error message

                                    else:

                                        subscriber = Subscribers(mobile_number=message['from'],
                                                                 subscribed_topic=username)
                                        subscriber.save()
                                        print("Subscriber saved successfully")
                                        response = "You have successfully subscribed to {} channel. You can send" \
                                                   "a message to this channel starting with the word {} " \
                                                   "followed by your message".format(username, username)
                                        sms_responses(message['from'], response)
                                        # check if the subscriber already exists. Not done, but will be done later
                                        # if the subscriber doesn't exist then save the subscriber
                                        # else if a subscriber already exists then call the send message
                                        # function and send a message stating that he/she is already subscribed to
                                        # that user

                            elif ratio1 >= 0.8 :
                                # if user does not exists get all the names that have a ratio of 0.7 and above

                                # check if the message already exists in our database
                                if Insms.objects.filter(msg_number=message['id'], keyword=username,
                                                        msg_type_status=False):
                                    print("Msg Type= Subscribe msg This message already exists in our database")
                                else:

                                    new_msg = Insms(sender=message['from'],
                                                    to=message['to'],
                                                    date=message['date'],
                                                    text=message['text'],
                                                    polarity=polarity(message['text']),
                                                    keyword="SPOILT_MSG",
                                                    msg_number=message['id'],
                                                    msg_read_status=True,
                                                    msg_type_status=False)
                                    new_msg.save()
                                    err_response = "No such channel. Did you mean {}".format(username)
                                    sms_responses(message['from'], err_response)

                            else:

                                # check if the message already exists in our database
                                if Insms.objects.filter(msg_number=message['id'], keyword=username,
                                                        msg_type_status=False):
                                    print("Msg Type= Subscribe msg This message already exists in our database")
                                else:

                                    new_msg = Insms(sender=message['from'],
                                                    to=message['to'],
                                                    date=message['date'],
                                                    text=message['text'],
                                                    polarity=polarity(message['text']),
                                                    keyword="SPOILT_MSG",
                                                    msg_number=message['id'],
                                                    msg_read_status=True,
                                                    msg_type_status=False)
                                    new_msg.save()

                    # This received sms function will be a task handled by celery and will be running every second
                    # n:b remember that this function does not return anything, it doesn't have to
                    else:
                        for username in usernames:
                            keyword2 = keywords[0]
                            ratio = sequence_match_ratio(keyword2, username.username)
                            print ("The match ratio in the text message to read is {}".format(ratio))
                            if Insms.objects.filter(msg_number=message['id'], keyword=username, msg_type_status=False):
                                print("Msg Type= txt message  This message already exists in our database")

                            else:
                                if ratio >= 0.6:
                                    text = Insms(  sender=message['from'],
                                                   to=message['to'],
                                                   date=message['date'],
                                                   text=message['text'],
                                                   polarity=polarity(message['text']),
                                                   keyword=username,
                                                   msg_number=message['id'],
                                                   msg_read_status=False,
                                                   msg_type_status=True)
                                    text.save()

                                else:
                                    text = Insms(sender=message['from'],
                                                 to=message['to'],
                                                 date=message['date'],
                                                 text=message['text'],
                                                 polarity=polarity(message['text']),
                                                 keyword="SPOILT_UNAME",
                                                 msg_number=message['id'],
                                                 msg_read_status=True,
                                                 msg_type_status=False)
                                    text.save()
                                    continue

                    lastReceivedId = message['id']

                else:
                    print ("No message in the africastalking cloud at the moment")
            if len(messages) == 0:
                    break

    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while fetching messages: %s' % str(e)



def smscount(smsCount):
    # this function does not accept any argument
    # smscount then will be a variable that holds all the sms in insms filtered with the keyword of the user's username
    smsCount2 = len(smsCount)
    return (smsCount2)


def posisms(messages1):
    # this function does not accept any argument
    # messages1 will then be a variable that holds all the sms in insms filtered with the keyword of the user's username
    posisms = 0
    for sms in messages1:
        if sms.polarity > 0:
            posisms +=1
    return (posisms)

def negsms(messages1):
    # this function also does not accept any argument
    # messages1 will then be a variable that holds all the sms in insms filtered with the keyword of the user's username
    negsms = 0
    for sms in messages1:
        if sms.polarity < 0:
            negsms +=1
    return (negsms)

def neutsms(messages1):
    # this function also does not accept any argument
    # messages1 will then be a variable that holds all the sms in insms filtered with the keyword of the user's username
    # nb if you get attribute error then take only one field of the insms table, that is the polarity field
    neutsms = 0
    for sms in messages1:
        if sms.polarity == 0:
            neutsms +=1
    return (neutsms)
