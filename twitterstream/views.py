from django.shortcuts import render

import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import time
from django.template import loader
from django.http import StreamingHttpResponse
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from pattern.web import Twitter, hashtags
from pattern.en import sentiment, polarity, subjectivity, positive
import json
from datetime import datetime
from django.db.models import Q
from django.core import serializers
from models import StreamTweets
from django.views.decorators.csrf import ensure_csrf_cookie

def streamfunction():
    global jsonData1
    jsonData1 = []
    # It might take a few seconds to set up the stream.
    stream = Twitter().stream("love", timeout=30)


    # while True:
    for i in range(100000):
        print i
        # Poll Twitter to see if there are new tweets.
        stream.update()
        # The stream is a list of buffered tweets so far,
        # with the latest tweet at the end of the list.
        for tweet in reversed(stream):
            sentimentpolarity = polarity(tweet.text)
            print tweet.text
            print tweet.language
            print tweet.author
            print tweet.date

            jsonData1.append(
                {'text': tweet.text, 'author': tweet.author, 'date': tweet.date, 'hashtags': hashtags(tweet.text),
                 'sentiments': sentimentpolarity})
            obj, created = StreamTweets.objects.get_or_create(text=tweet.text, author=tweet.author, polarity=polarity(tweet.text))
            print created
        # Clear the buffer every so often.
        stream.clear()
        # Wait awhile between polls.
        time.sleep(1)

    return jsonData1



def streaming(request):

    obj = StreamTweets.objects.last()
    streamtweets = serializers.serialize('json', [obj, ])
    struct = json.loads(streamtweets)
    data = json.dumps(struct[0])
    return JsonResponse({"data":[data]})


def streaming1(request):
    id = request.GET.get('id', '')
    if id is not None:
        obj = StreamTweets.objects.get(id=7)
        streamtweets = serializers.serialize('json', [obj,])
        struct = json.loads(streamtweets)
        data = json.dumps(struct[0])
        return HttpResponse(data, content_type='json')



def streaming23(request):

    obj = StreamTweets.objects.last()
    #today = datetime.now()
    #data = StreamTweets.objects.filter(Q(date=today))
    #streamtweets = serializers.serialize('json', [obj, ])
    struct = json.loads(obj)
    data = json.dumps(struct[0])
    results = [ob.as_json() for ob in data]
    return HttpResponse(json.dumps(results), content_type="application/json")



@ensure_csrf_cookie
def stream(request):
    #streamfunction()
    # jsonData1 = StreamTweets.objects.all()
    # data = StreamTweets.objects.latest('id')
    title = "Stream data"
    template = loader.get_template('twitterstream/stream.html')
    context = {"title": title}
    return HttpResponse(template.render(context, request))




















