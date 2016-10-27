from models import Topics, KeyWords
from django.http import HttpResponse
from django.template import loader
from .forms import SearchForm

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
from pattern.en import sentiment, polarity, subjectivity, positive
import json

from searchfunction import searchingfunction
from django.shortcuts import redirect




# def topic_to_keywords(request):
#     topic = request.GET.get('topic')
#     ret = []
#     title = "Search"
#     template = loader.get_template('search/search.html')
#     form = CascadeForm(request.GET or None)
#     context = {"form": form, "title": title}
#
#     if topic:
#         for keywords in KeyWords.objects.filter(topic_id=topic):
#             ret.append(dict(id=keywords.key_word_id, value=unicode(keywords)))
#     if len(ret)!=1:
#         ret.insert(0, dict(id='', value='---'))
#
#     return HttpResponse(simplejson.dumps(ret))







def searchwordview(request):
    global jsonData
    jsonData = []
    title = "Search"
    template = loader.get_template('search/search.html')
    if request.method == 'GET':
        form = SearchForm()

    else:
        form = SearchForm(request.POST)

        if form.is_valid():
            newsearchword = request.POST['searchword']

            try:
                table = Datasheet.load(pd("sammy.csv"))
                index = set(table.columns[0])

            except:
                table = Datasheet()
                index = set()

            engine = Twitter(language="en")

            prev = None

            for i in range(2):
                print i

                for tweet in engine.search(newsearchword, start=prev, count=10, cached=False):
                    print
                    print tweet.text
                    print tweet.author
                    print tweet.date
                    print hashtags(tweet.text)
                    print sentiment(tweet.text)
                    print polarity(tweet.text)
                    print

                    global newdata
                    jsonData.append({'text':tweet.text, 'author':tweet.author, 'date':tweet.date, 'hashtags':hashtags(tweet.text),
                                     'sentiments':sentiment(tweet.text), 'polarity':polarity(tweet.text)})

                    if len(table) == 0 or tweet.id not in index:
                        table.append([tweet.id, tweet.text])
                        index.add(tweet.id)

                    prev = tweet.id

            #table.save(pd("sammy.csv"))

            print "Total results:  ", len(table)
            print
        #return HttpResponse(json.dumps(jsonData))
        return redirect("results/")


    context = {"form": form, "title": title}
    return HttpResponse( template.render(context, request))

def results(jsonData1):
    jsonData2 =searchingfunction(jsonData1)
    template = loader.get_template('search/results.html')
    context = { "newdata":jsonData2}
    return HttpResponse( template.render(context))