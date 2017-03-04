

import tweepy
import json



def fetch_tweets(q,dateFrom,dateTo):
    consumer_key = '7lO82bYVdJC9BTyqOGUnrXh5M'
    consumer_secret = 'TN2eCN33TRaKGSZRtXGBL5xccGljLzx6h2wiAnFVs4hQhP1DZG'
    access_token = '809545887399706624-m6Fp4Vw8Xkezm0d88yyr13qfJAtpoKj'
    access_secret = 'UnumW6OLy1FIa2wXs4hU8c3qUfTbsrwoYLvsrzymxk6WS'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # set up twitter api OAut token
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    print api
    max_tweets = 11     # eliminate the number of tweets to control the process as a draft
    #searched_tweets = [status.text.encode('utf-8') for status in tweepy.Cursor(api.search, q=q).items(max_tweets)]   "5.29126,52.132633,250km"
    searched_tweets = [status for status in tweepy.Cursor(api.search,q=q,since= dateFrom ,until= dateTo).items(max_tweets)]

    tweets_data = []
    for line in searched_tweets:
        alltweetvalues = [str(line.user.screen_name.encode('utf-8')), str(line.created_at),str(line.text.encode('utf-8'))]
        tweets_data.append(alltweetvalues)    # encoding text data

    return tweets_data









#q= "saw"
#print fetch_tweets(q=q)
