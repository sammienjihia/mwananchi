from models import Topics, KeyWords
import os
from django.http import HttpResponse
from django.template import loader
from .forms import SearchForm

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
from pattern.en import sentiment, polarity, subjectivity, positive
import json

#from searchfunction import searchingfunction
from django.core import serializers
import vincent
from searchfunction2 import searchfunction2
from searchfunction2 import tweetcount
from searchfunction2 import getusersearchword
from django.shortcuts import redirect





def searchwordview(newsearchword1):
    global jsonData
    jsonData = []
    title = "Search"
    template = loader.get_template('search/search.html')
    form = SearchForm()
    searchingword = getusersearchword(newsearchword1)
    print searchingword
    if searchingword:
        return redirect("results/")
    else:
        print "getusersearchword() returned an empty object"
    # if request.method == 'GET':
    #     form = SearchForm()
    #
    # else:
    #     form = SearchForm(request.POST)
    #
    #     if form.is_valid():
    #         newsearchword = request.POST['searchword']
        #searchingfunction(newsearchword)

        #return redirect("results/")


    context = {"form": form, "title": title}
    return HttpResponse( template.render(context, newsearchword1))

def results(newsearchword):
    tweetdate = []
    #jsonData2 = searchingfunction(newsearchword)
    jsonData2, postweets2, negtweets2, neutweets2, word_freq, time_series = searchfunction2()

    labels, freq = zip(*word_freq)
    data = {'data': freq, 'x': labels}
    print data
    bar = vincent.Bar(data, iter_idx='x')
    print bar
    bar.to_json('term4_freq.json')
    print bar.to_json()

    time_chart = vincent.Line(time_series)
    time_chart.axis_titles(x='Time', y='Freq')
    time_chart.legend(title='Matches')
    time_chart.to_json('time_chart.json')
    print time_chart.to_json()




    #postweets2 = postweets()
    #negtweets2 = negtweets()
    #neutweets2 = neutweets()
    tweetcount3 = tweetcount(jsonData2)
    template = loader.get_template('search/results.html')
    context = { "newdata":jsonData2, "tweetcount":tweetcount3, "postweets": postweets2, "negtweets": negtweets2, "neutweets": neutweets2, "bar2": bar, "jsonbar": bar.to_json(), "timeseries": time_chart.to_json()}
    return HttpResponse( template.render(context))