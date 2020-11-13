# USING TWITTER'S APIs THROUGH A DEVELOPER ACCOUNT, I LEARNED HOW DATA MINING IS APPLIED AND USED.  
import keys
import tweepy as t 

auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = t.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.get_user("prattprattpratt") # put in username

print(user.name)

print(user.description)

print(user.status.text)

print(user.followers_count)

print(user.geo_enabled)

print()

me = api.me

#print(me.name)

followers = []

#print(user)

cursor = t.Cursor(api.followers, screen_name ="prattprattpratt")

for account in cursor.items(10): # gets followers
    followers.append(account.screen_name)


print(followers)

friends = [] 

cursor = t.Cursor(api.friends, screen_name = "prattprattpratt") # see who he follows

for friend in cursor.items(10):
    friends.append(friend.screen_name)

print(friends)

# Getting a user's recent tweets.
# the API method user_timeline returns tweets from the
# timeline of a specific account. 

chris_tweets = api.user_timeline(screen_name = 'prattprattpratt', count = 5)

#for tweet in chris_tweets:
#   print(f'{tweet.user.screen_name}: {tweet.text}\n')

mytweets = api.home_timeline()

for tweet in mytweets:
    print(f'{tweet.text}\n')
