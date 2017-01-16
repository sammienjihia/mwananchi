import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import time
from pattern.web import Twitter, hashtags
from pattern.en import sentiment, polarity, subjectivity, positive
from models import StreamTweets


def streamfunction():
    global jsonData1
    jsonData1 = []
    # It might take a few seconds to set up the stream.
    stream = Twitter().stream("waititu", timeout=30)


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
            obj, created = StreamTweets.objects.get_or_create(text=tweet.text, author=tweet.author, polarity=polarity(tweet.text), date=tweet.date)
            print created
        # Clear the buffer every so often.
        stream.clear()
        # Wait awhile between polls.
        time.sleep(1)

    return jsonData1
