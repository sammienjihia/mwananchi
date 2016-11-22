from models import Topics, KeyWords
from django.http import HttpResponse
from django.template import loader
from .forms import SearchForm

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
from pattern.en import sentiment, polarity, subjectivity, positive
import json

from searchfunction import searchingfunction
from searchfunction import tweetcount
from searchfunction import postweets, negtweets, neutweets, getusersearchword
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

    jsonData2 = searchingfunction(newsearchword)


    postweets2 = postweets(postweets)
    negtweets2 = negtweets(negtweets)
    neutweets2 = neutweets(neutweets)
    tweetcount3 = tweetcount(jsonData2)
    template = loader.get_template('search/results.html')
    context = { "newdata":jsonData2, "tweetcount":tweetcount3, "postweets": postweets2, "negtweets": negtweets2, "neutweets": neutweets2}
    return HttpResponse( template.render(context))