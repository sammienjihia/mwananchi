from models import Topics, KeyWords
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import SearchForm

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
from pattern.en import sentiment, polarity, subjectivity, positive
import json

#from searchfunction import searchingfunction
from django.core import serializers
from django.shortcuts import render
import vincent
from searchfunction2 import searchfunction2
from searchfunction2 import tweetcount
from searchfunction2 import getusersearchword
from django.shortcuts import redirect
from vincent import AxisProperties, PropertySet, ValueRef





def searchwordview(request):
    global jsonData
    jsonData = []
    title = "Search"
    template = loader.get_template('search/search.html')
    if request.method == 'POST':
        request.session['searchword'] = request.POST['searchword']
        return HttpResponseRedirect("results/")
    else:
        return render(request, 'search/search.html')


def results(request):
    tweetdate = []
    searchword = request.session.get('searchword')
    jsonData2, postweets2, negtweets2, neutweets2, hash_freq, word_freq, time_series = searchfunction2(searchword)

    labels, freq = zip(*hash_freq)
    data = {'data': freq, 'x': labels}
    bar = vincent.Bar(data, iter_idx='x')
    bar.axis_titles(x='Hashtags', y='Frequency')
    bar.to_json('term4_freq.json')
    ax = AxisProperties(
        labels=PropertySet(angle=ValueRef(value=11)))
    bar.axes[0].properties = ax

    labels, freq = zip(*word_freq)
    data = {'data': freq, 'x': labels}
    bar2 = vincent.Bar(data, iter_idx='x')
    bar2.to_json('term5_freq.json')


    time_chart = vincent.Line(time_series)
    time_chart.axis_titles(x='Time', y='Freq')
    time_chart.legend(title='Tweets as data')
    time_chart.to_json('time_chart.json')

    print ()
    print("This is the time series")
    print(time_chart.to_json('time_chart.json'))


    tweetcount3 = tweetcount(jsonData2)
    template = loader.get_template('search/results.html')
    context = { "searchword":searchword, "newdata":jsonData2, "tweetcount":tweetcount3, "postweets": postweets2, "negtweets": negtweets2, "neutweets": neutweets2, "bar2": bar, "jsonbar": bar.to_json(), "jsonbar2": bar2.to_json(), "timeseries": time_chart.to_json()}
    return HttpResponse( template.render(context))