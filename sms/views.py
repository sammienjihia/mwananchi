from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from search.models import Topics
from subscribe.models import Subscribers
from .forms import SendsmsForm
from django.shortcuts import render, redirect
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)



# Create your views here.



def sendsmsview (request):
    title = "Send Message"
    template = loader.get_template('sms/sendsmsform.html')
    form = SendsmsForm(request.POST or None)
    if request.method == 'POST':
        #form = SendsmsForm(request.POST or None)
        if form.is_valid():
            subscribb_topic = request.POST['subscribed_topic']


            username = "MyAfricasTalkingUsername"
            apikey = "MyAfricasTalkingAPIKey"

            # numbers = Subscribers.objects.values_list('mobile_number', flat=True).distinct()
            # Topics.objects.values_list('topic_id', flat=True)

            # to get the mobile numbers that are subscribed to topic id 1 use the below code
            numbers = Subscribers.objects.filter(subscribed_topic_id=subscribb_topic).values_list('mobile_number',
                                                                                                 flat=True).distinct()

            to = numbers

            message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

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

            return HttpResponse( subscribb_topic)

    context = {"form": form, "title": title}
    return HttpResponse(template.render(context, request))




