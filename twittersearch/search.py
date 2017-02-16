from pattern.web import Twitter, hashtags
from pattern.db import Datasheet, pprint, pd

try:
    table = Datasheet.load(pd("sammy.csv"))
    index = set(table.columns[0])


except:
    table = Datasheet()
    index = set()

engine = Twitter(language="en")

#item = raw_input("Please enter a twittersearch key word")
prev = None

for i in range(2):
    print i
    for tweet in engine.search("", start=prev, count=25, cached=False):
        print
        print tweet.text
        print tweet.author
        print tweet.date
        print hashtags(tweet.text)
        print

        if len(table) == 0 or tweet.id not in index:
            table.append([tweet.id, tweet.text])
            index.add(tweet.id)

        prev = tweet.id

table.save(pd("sammy.csv"))

print "Total results:  ", len(table)
print

pprint(table, truncate=100)
