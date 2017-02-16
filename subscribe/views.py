from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from twittersearch.models import Topics
from .forms import SubscriptionForm
from django.shortcuts import render, redirect


# Create your views here.



def subscriptionview (request):
    title = "Subscribe"
    template = loader.get_template('subscribe/subscriptionform.html')
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        subscriber = form.save()
        #answer = form.cleaned_data.get('subscribed_topic')
        subscriber.save()

        return HttpResponse("successfully subscribed ")



    context = {"form": form, "title": title}
    return HttpResponse(template.render(context, request))






