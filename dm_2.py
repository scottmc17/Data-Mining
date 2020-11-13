import keys
import tweepy as t 
import json
from wordcloud import WordCloud



auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = t.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets = api.search(q="vote", count=3)

#print(tweets)

# Excercise - based om the object created above, print out the screen name 
# user and the text of the tweet

'''
for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text)  

tweets = api.search(q = "#collegefootball", count =2)

for tweet in tweets:
    print(tweet.user.screen_name, ":", tweet.text)
'''
# Places with Trending Topics

trends_available = api.trends_available()

#print(len(trends_available))

#print(trends_available[:3])  # trends_available is a list of dicts

world_trends = api.trends_place(id = 1)

#print(world_trends)

outfile = open('world_trends.json', 'w')

json.dump(world_trends, outfile, indent = 5)

trends_list = world_trends[0]['trends']

#print(trends_list)

# Excercise
# using list comprehension grab those trends that 
# have more than 10,000 tweets
'''
trends_list = [t for t in trends_list if t["tweet_volume"]]

from operator import itemgetter

trends_list.sort(key = itemgetter("tweet_volume"), reverse = True)

print(trends_list[:5])

print out the name of the topic for the 5 top topics.

for trend in trends_list[:5]:
    #print(trend["name"])
'''

# Excercise
# Find the trending topics for New York City and
# create a wordcloud from it New York City  Trending Topics


nyc_trends = api.trends_place(id=2459115)

nyc_trends_list = nyc_trends[0]['trends']

nyc_trends_list = [t for t in nyc_trends_list if t["tweet_volume"]]

from operator import itemgetter

nyc_trends_list.sort(key = itemgetter("tweet_volume"), reverse = True)

topics = {} #create empty dictionary 

for trend in nyc_trends_list:
    #print(trend)
    topics[trend["name"]] = trend["tweet_volume"]


wordcloud = WordCloud(
    width=1600,
    height=900,
    prefer_horizontal=0.5,
    min_font_size=10,
    colormap="prism",
    background_color="white",
)


wordcloud = wordcloud.fit_words(topics)

wordcloud = wordcloud.to_file("TrendingTwitter_fall2020.png")



