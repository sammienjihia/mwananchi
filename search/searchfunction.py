
from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
from pattern.en import sentiment, polarity, subjectivity, positive
import json
from django.http import HttpResponse



def getusersearchword(request):
    global newsearchword1
    newsearchword1 = ""

    if (request.method == 'POST'):
        newsearchword1 = request.POST['searchword']

    return newsearchword1



def searchingfunction(newsearchword):

    newsearchword1


    jsonData1 = []
    global sentimentpolarity

    try:
        table = Datasheet.load(pd("sammy.csv"))
        index = set(table.columns[0])

    except:
        table = Datasheet()
        index = set()

    engine = Twitter(language="en")

    prev = None
    #newsearchword = "Sammy"

    for i in range(2):
        print i

        for tweet in engine.search(newsearchword1, start=prev, count=300, cached=False):


            sentimentpolarity = polarity(tweet.text)



            jsonData1.append({'text':tweet.text, 'author':tweet.author, 'date':tweet.date, 'hashtags':hashtags(tweet.text), 'sentiments':sentimentpolarity})

            if len(table) == 0 or tweet.id not in index:
                table.append([tweet.id, tweet.text])
                index.add(tweet.id)

            prev = tweet.id


    #return (json.dumps(jsonData1))
    return (jsonData1)

def tweetcount(tweetCount):
    tweetCount2 = len(tweetCount)
    return (tweetCount2)

def postweets(jsonData1):
    postweets = 0
    for tweet in searchingfunction(jsonData1):
        if polarity(tweet['text']) > 0:
            postweets +=1
    return (postweets)

def negtweets(jsonData1):
    negtweets = 0
    for tweet in searchingfunction(jsonData1):
        if polarity(tweet['text']) < 0:
            negtweets +=1
    return (negtweets)

def neutweets(jsonData1):
    neutweets = 0
    for tweet in searchingfunction(jsonData1):
        if polarity(tweet['text']) == 0:
            neutweets +=1
    return (neutweets)



