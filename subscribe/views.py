from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from search.models import Topics
from .forms import SubscriptionForm
from django.shortcuts import render, redirect


# Create your views here.

def subscriptionview(request):
    TOPIC_CHOICES = Topics.objects.all()




    #subscription = request.POST['subscribe']
    subscription = request.POST.get("subscribe", "Guest (or whatever)")

    template = loader.get_template('subscribe/subscriptionform.html')
    context = {"subscription": subscription}

    return HttpResponse(template.render(context, request))

def subscriptionview (request):
    title = "Subscribe"
    template = loader.get_template('subscribe/subscriptionform.html')
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        subscriber = form.save()
        #answer = form.cleaned_data.get('subscribed_topic')
        subscriber.save()

        return redirect("/index")



    context = {"form": form, "title": title}
    return HttpResponse(template.render(context, request))






