
import tweepy
import json
from APICodes import TOKEN
from APICodes import TOKEN_SECRET
from APICodes import CONSUMER_SECRET
from APICodes import CONSUMER_KEY

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(CONSUMER_KEY,TOKEN_SECRET)

api = tweepy.API(auth)

for tweet in api.search(q="covid vaccine", lang="en", rpp=10):
    print(f"{tweet.user.name}: {tweet.text}")

