from django.shortcuts import render

import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import time
import urllib
from django.template import loader
from search.searchfunction2 import getusersearchword
from django.http import StreamingHttpResponse
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse, Http404
from pattern.web import Twitter, hashtags
from pattern.en import sentiment, polarity, subjectivity, positive
import json
from datetime import datetime
from django.shortcuts import render, redirect
from forms import StreamForm, DownloadForm
from django.db.models import Q
from django.core import serializers
from models import StreamTweets
from django.views.decorators.csrf import ensure_csrf_cookie
from streamming import streamfunction


# def streaming(request):
#
#     obj = StreamTweets.objects.last()
#     streamtweets = serializers.serialize('json', [obj, ])
#     struct = json.loads(streamtweets)
#     data = json.dumps(struct)
#     return JsonResponse({"data":data})
#
#
# def streaming1(request):
#     id = request.GET.get('id', '')
#     if id is not None:
#         obj = StreamTweets.objects.get(id=7)
#         streamtweets = serializers.serialize('json', [obj,])
#         struct = json.loads(streamtweets)
#         data = json.dumps(struct[0])
#         return HttpResponse(data, content_type='json')
#
#
#
# def streaming23(request):
#
#     obj = StreamTweets.objects.last()
#     #today = datetime.now()
#     #data = StreamTweets.objects.filter(Q(date=today))
#     #streamtweets = serializers.serialize('json', [obj, ])
#     struct = json.loads(obj)
#     data = json.dumps(struct[0])
#     results = [ob.as_json() for ob in data]
#     return HttpResponse(json.dumps(results), content_type="application/json")
#



from django.conf import settings
from django.http import HttpResponse

import json
import time
import datetime
from pattern.web import Twitter
from pattern.db import Datasheet, pprint, pd


def tweetstream(request):
    title = "Start stream bot"
    template = loader.get_template('twitterstream/form.html')
    form = StreamForm(request.POST or None)
    context = {"form": form, "title": title}

    if form.is_valid():
        searchword = form.cleaned_data.get("searchword")
        filename = form.cleaned_data.get('filename')
        timedelta = form.cleaned_data.get('timedelta')



        #return HttpResponse(template.render(context, request))



        base = datetime.datetime.now()
        numdays = timedelta
        new_time = base + datetime.timedelta(minutes=numdays)
        timedif = new_time - base
        newtimedif = int(timedif.total_seconds())
        print newtimedif
        print "File path:", pd('%s.json' % filename, 'wb')

        try:
            # We'll store tweets in a Datasheet.
            # A Datasheet is a table of rows and columns that can be exported as a CSV-file.
            # In the first column, we'll store a unique id for each tweet.
            # We only want to add the latest tweets, i.e., those we haven't seen yet.
            # With an index on the first column we can quickly check if an id already exists.
            # The pd() function returns the parent directory of this script + any given path.
            table = Datasheet.load(pd('%s.json' % filename, 'wb'))
            index = set(table.columns[0])
        except:
            table = Datasheet()
            index = set()

        # Another way to mine Twitter is to set up a stream.
        # A Twitter stream maintains an open connection to Twitter,
        # and waits for data to pour in.
        # Twitter.search() allows us to look at older tweets,
        # Twitter.stream() gives us the most recent tweets.

        # It might take a few seconds to set up the stream.
        stream = Twitter().stream(searchword, timeout=30)

        # while True:
        for i in range(newtimedif):
            print i
            # Poll Twitter to see if there are new tweets.
            stream.update()
            # The stream is a list of buffered tweets so far,
            # with the latest tweet at the end of the list.
            for tweet in reversed(stream):
                print tweet.text
                print tweet.language
                print tweet.author
                print tweet.date
                sentimentpolarity = polarity(tweet.text)
                # Only add the tweet to the table if it doesn't already exists.
                if len(table) == 0 or tweet.id not in index:
                    table.append([tweet.id, tweet.text, tweet.author, tweet.date,
                          hashtags(tweet.text), sentimentpolarity])
                    index.add(tweet.id)
                # Continue mining older tweets in next iteration.
                prev = tweet.id
                # Create a .csv in pattern/examples/01-web/
                table.save(pd('%s.json' % filename))


            # Clear the buffer every so often.
            stream.clear()
            # Wait awhile between polls.
            time.sleep(1)

        if pd('%s.json' % filename, 'wb'):
            with open(pd('%s.json' % filename)) as fh:
                response = HttpResponse(fh.read(), content_type="application/json")
                response['Content-Disposition'] = 'attachment; filename=' + pd('%s.json' % filename)
                return response
        else:
            raise Http404



    return HttpResponse(template.render(context, request))

def download(request):
    title = "Download your file"
    template = loader.get_template('twitterstream/form.html')
    form = DownloadForm(request.POST or None)
    context = {"form": form, "title": title}
    if request.method == 'POST':
        if form.is_valid():
            filename = form.cleaned_data.get('filename')

            # testfile = urllib.URLopener()
            # urllib.urlretrieve(pd('%s.json' % filename), ('%s.json' % filename))

            if pd('%s.json' % filename, 'wb'):
                with open(pd('%s.json' % filename)) as fh:
                    response = HttpResponse(fh.read(), content_type="application/json")
                    response['Content-Disposition'] = 'attachment; filename=' + pd('%s.json' % filename)
                    return response
            else:
                raise Http404
    else:
        return HttpResponse(template.render(context, request))


@ensure_csrf_cookie
def stream(request):
    #streamdata = streamfunction()
    # jsonData1 = StreamTweets.objects.all()
    # data = StreamTweets.objects.latest('id')
    title = "Stream data"
    template = loader.get_template('twitterstream/stream.html')
    context = {"title": title, "streamdata": ""}
    return HttpResponse(template.render(context, request))




















