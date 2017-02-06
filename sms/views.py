from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from search.models import Topics
from subscribe.models import Subscribers
from .models import Insms, Outsms, Blacklistsms, Failedsms
from .forms import SendsmsForm
from django.shortcuts import render, redirect
from mwananchi.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from sendtext import receivedsms, smscount, posisms, negsms, neutsms
from sendtext import getusersearchword
from .forms import SmssearchForm
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required




# Create your views here.

def smssearchwordview(newsearchword1):
    global searchingword, option
    searchingword = ""
    option = ""
    title = "Search"
    template = loader.get_template('sms/smssearch.html')
    form = SmssearchForm()
    searchingword, option = getusersearchword(newsearchword1)
    print searchingword
    print option
    if searchingword:
        return redirect("insms/")
    else:
        print "getusersearchword() returned an empty object"

    context = {"form": form, "title": title}
    return HttpResponse( template.render(context, newsearchword1))



def sendsmsview (request):
    title = "Send Message"
    template = loader.get_template('sms/sendsmsform.html')
    form = SendsmsForm(request)
    if request.method == 'POST':
        form = SendsmsForm(request, request.POST)
        #form = SendsmsForm(request.POST or None)
        if form.is_valid():
            subscribb_topic = request.POST['subscribed_topic']
            messagein = request.POST['message']


            username = "SAMMIENJIHIA"
            apikey = "9898e481449e39a6051b3d87e07f4de171bedc93a046dd166c0dad2d0d9b6bdc"


            # numbers = Subscribers.objects.values_list('mobile_number', flat=True).distinct()
            # Topics.objects.values_list('topic_id', flat=True)

            # to get the mobile numbers that are subscribed to topic id 1 use the below code
            numbers = Subscribers.objects.filter(subscribed_topic_id=subscribb_topic).values_list('mobile_number',
                                                                                                 flat=True).distinct()

            #to = numbers

            numbersto = [numbers.encode("utf8") for numbers in
                            Subscribers.objects.filter(subscribed_topic_id=subscribb_topic).values_list('mobile_number',
                                                                                                        flat=True).distinct()]
            for number in numbersto:



                to = number

                #message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
                message = messagein

                gateway = AfricasTalkingGateway(username, apikey)

                try:

                    results = gateway.sendMessage(to, message)


                    for recipient in results:
                        # status is either "Success" or "error message"
                        print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                            recipient['status'],
                                                                            recipient['messageId'],
                                                                            recipient['cost'])

                        if recipient['status'] == "Success":
                            sentdata = Outsms(sender=request.user.id, receiver=recipient['number'], sent_date=datetime.now(), text=messagein)
                            sentdata.save()

                        elif recipient['status'] == "error message":
                            msgerror = Failedsms(sender=request.user.id, receiver=recipient['number'],
                                              sent_date=datetime.now(), text=messagein)
                            msgerror.save()

                        elif recipient['status'] == "User In BlackList":
                            blacklistsms = Blacklistsms(sender=request.user.id, receiver=recipient['number'],
                                                 sent_date=datetime.now(), text=messagein)
                            blacklistsms.save()


                except AfricasTalkingGatewayException, e:
                    print 'Encountered an error while sending: %s' % str(e)


    context = {"form": form, "title": title}
    return HttpResponse(template.render(context, request))


def insmsview(messages1):
    global messages3
    print option
    messages3 = ""

    if option == "1":
        N = 30000
        start_date = datetime.now()
        date_N_days_ago = datetime.now() - timedelta(days=N)
        messages3 = Insms.objects.filter(keyword=searchingword, date__range=(date_N_days_ago, start_date))

    elif option == "2":
        print "hahahahhahahah"
        N = 7
        start_date = datetime.now()
        date_N_days_ago = datetime.now() - timedelta(days=N)
        messages3 = Insms.objects.filter(keyword=searchingword, date__range=(date_N_days_ago, start_date))
    elif option =="3":
        N = 30
        start_date = datetime.now()
        date_N_days_ago = datetime.now() - timedelta(days=N)
        messages3 = Insms.objects.filter(keyword=searchingword, date__range=(date_N_days_ago, start_date))
    elif option =="4":
        N = 360
        start_date = datetime.now()
        date_N_days_ago = datetime.now() - timedelta(days=N)
        messages3 = Insms.objects.filter(keyword=searchingword.lower(), date__range=(date_N_days_ago, start_date))
    else:
        print "you have not selected anything"

    #messages3 = Insms.objects.filter(keyword=searchingword)
    smscount1 = smscount(messages3)
    posisms1 = posisms(messages3)
    negsms1 = negsms(messages3)
    neutsms1 = neutsms(messages3)
    messages2 = receivedsms(messages1)
    template = loader.get_template('sms/results.html')
    context = {"inmessages": messages3, "smscount": smscount1, "posisms": posisms1, "negsms": negsms1, "neutsms": neutsms1}
    return HttpResponse(template.render(context))




