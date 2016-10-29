
from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
from pattern.en import sentiment, polarity, subjectivity, positive
import json
from django.http import HttpResponse














def searchingfunction(jsonData):


    jsonData1 = []





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

        for tweet in engine.search("wake", start=prev, count=5, cached=False):


            sentimentpolarity = polarity(tweet.text)



            jsonData1.append({'text':tweet.text, 'author':tweet.author, 'date':tweet.date, 'hashtags':hashtags(tweet.text), 'sentiments':sentimentpolarity})

            if len(table) == 0 or tweet.id not in index:
                table.append([tweet.id, tweet.text])
                index.add(tweet.id)

            prev = tweet.id



    print "Total results:  ", len(table)



    #return (json.dumps(jsonData1))
    return (jsonData1)

