import tweepy
import json
from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd

from pattern.en import sentiment, polarity, subjectivity, positive
import operator
import json
from sort import bubble
from collections import Counter
from preprocess import preprocess
from nltk.corpus import stopwords
import string
import pandas

import re

ckey = "DASDze82n52S1mWqjaABSOFZD"
csecret = "VjDDbowV4qEHdn0v5f8IkiWNwzYlozmww11fularNSpF1t4jqD"
atoken = "617272510-yeKlMicDSRCaG4caycA7VoFZRTjjwsyPoKVz2QMl"
asecret = "Dfcvt6N1PBvSwAQdMQYsQhedwQYa4wL90oCkLAYKyRBVY"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)


#start ---convert api data into jason object

#jason.loads(cricTweet)
#end conversion


#This function will get users search words
def getusersearchword(request):

    newsearchword1 = ""

    global newsearchword1

    if (request.method == 'POST'):
        newsearchword1 = request.POST['searchword']

    return newsearchword1



#This function will search your query in twitter

def searchfunction2(newsearchword1):
    jsonData1 = []
    negtweets = 0
    postweets = 0
    neutweets = 0
    dates_ITAvWAL = []

    global sentimentpolarity

    try:
        table = Datasheet.load(pd("sammy.csv"))
        index = set(table.columns[0])

    except:
        table = Datasheet()
        index = set()

    query = newsearchword1
    prev = None
    count_all = Counter()
    count_all2 = Counter()

    #for tweet in (tweepy.Cursor(api.search, q=newsearchword1, cached=False, start=prev).items(20)):
    for tweet in api.search(q=newsearchword1, cached=False, start=prev, count=100):

        print
        print
        print ("Date:", tweet.created_at)
        print ("Username:", tweet.user.name)
        print ("Screen name:", tweet.user.screen_name)
        print ("Tweet:", tweet.text)
        print ("Polarity:", polarity(tweet.text))
        print ("Subjectivity:", subjectivity(tweet.text))
        print ("Language:", tweet.lang)
        print ("Retwwet Count:", tweet.retweet_count)
        print ("User follower count:", tweet.user.followers_count)
        print ("Location", tweet.user.location)
        print ("Favourites Count:", tweet.user.favourites_count)
        print ("Hash tags:", hashtags(tweet.text))
        print
        print
        sentimentpolarity = polarity(tweet.text)


        jsonData1.append({'tweetid': tweet.id, 'text': tweet.text, 'author': tweet.user.screen_name, 'date': tweet.created_at,
                          'hashtags': hashtags(tweet.text), 'sentiments': sentimentpolarity, 'followers':tweet.user.followers_count,
                          'retweets':tweet.retweet_count, 'favourite': tweet.user.favourites_count })



        if sentimentpolarity > 0:
            postweets +=1

        elif sentimentpolarity < 0:
            negtweets += 1

        elif sentimentpolarity == 0:
            neutweets += 1

        else:
            print "Something went wrong while polling"


        punctuation = list(string.punctuation)
        ####################The below commented lines will help to search for the most frequent terms######
        stop = stopwords.words('english') + punctuation + ['rt', 'via']

        terms_only2 = [term for term in tweet.text.lower().split() if term not in stop and not term.startswith(('#', '@')) ]
        count_all2.update(terms_only2)
        print "here are the tokens"
        print terms_only2

        term = str(preprocess(tweet.text, lowercase=True))

        terms_only = re.findall(r'#\w+', term)
        termsw = "click me... http://127.0.0.1:8000/search/results/"
        # print ' '.join(terms_only2)
        # print termsw.split()

        count_all.update(terms_only)
        # terms_only = [term for term in preprocess(tweet.text, lowercase=True) if term.startswith('#')]
        # count_all.update(terms_only)

        if query.lower() in terms_only or terms_only2:
            dates_ITAvWAL.append(tweet.created_at)


        if len(table) == 0 or tweet.id not in index:
            table.append([tweet.id, tweet.text])
            index.add(tweet.id)

        prev = tweet.id



    ones = [1] * len(dates_ITAvWAL)

    idx = dates_ITAvWAL

    ITAvWAL = pandas.Series(ones, index=idx)
    # Resampling / bucketing
    per_hour = ITAvWAL.resample('1t').sum().fillna(0)




    return (jsonData1, postweets, negtweets, neutweets, count_all.most_common(10), count_all2.most_common(10), per_hour)


def tweetcount(tweetCount):
    tweetCount2 = len(tweetCount)
    return (tweetCount2)


