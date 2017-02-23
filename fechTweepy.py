import SMToolsLE

import tweepy
from tweepy import OAuthHandler


consumer_key = '7lO82bYVdJC9BTyqOGUnrXh5M'
consumer_secret = 'TN2eCN33TRaKGSZRtXGBL5xccGljLzx6h2wiAnFVs4hQhP1DZG'
access_token = '809545887399706624-m6Fp4Vw8Xkezm0d88yyr13qfJAtpoKj'
access_secret = 'UnumW6OLy1FIa2wXs4hU8c3qUfTbsrwoYLvsrzymxk6WS'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
#print api

query = SMToolsLE.keyword
max_tweets = 50
searched_tweets = [status.text.encode('utf-8') for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
print  searched_tweets