import tweepy
import json



def fetch_tweets(q):
    consumer_key = '7lO82bYVdJC9BTyqOGUnrXh5M'
    consumer_secret = 'TN2eCN33TRaKGSZRtXGBL5xccGljLzx6h2wiAnFVs4hQhP1DZG'
    access_token = '809545887399706624-m6Fp4Vw8Xkezm0d88yyr13qfJAtpoKj'
    access_secret = 'UnumW6OLy1FIa2wXs4hU8c3qUfTbsrwoYLvsrzymxk6WS'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    print api
    max_tweets = 2
    #searched_tweets = [status.text.encode('utf-8') for status in tweepy.Cursor(api.search, q=q).items(max_tweets)]   "5.29126,52.132633,250km"
    searched_tweets = [status for status in tweepy.Cursor(api.search,q=q,since="2017-2-16" ,until="2017-2-28").items(max_tweets)]
    #encoded_tweets = json.dumps(searched_tweets)
    tweets_data = []
    for line in searched_tweets:
            

            #neme = line.user.screen_name
            #creatDate =  line.created_at
            #tweet = line.text
            alltweetvalues = [str(line.user.screen_name.encode('utf-8')), str(line.created_at), str(line.text.encode('utf-8'))]
            tweets_data.append(alltweetvalues)

            print "----------------------------------------------------"
            print "----------------------------------------------------"
            #print type(lined)
            #print type(tweets)

    return tweets_data
    #print tweets_data


q= "saw"
lists = fetch_tweets(q=q)

for x in lists:
    print x[0]
    print '=================='
    print x[1]
    print '=================='
    print x[2]
    print '=================='
