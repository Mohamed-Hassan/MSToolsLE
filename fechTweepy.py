import re
import string
import CDictionary
import CONFIG
import tweepy


def cleanTweet(text):
    text = re.sub(r"http\s+", "",text)
    tbl = string.maketrans('','')
    text.translate(tbl,string.punctuation)
    text.lower()
    return text.split(' ')


def fetch_tweets(q,dateFrom,dateTo,city,wieght):
    consumer_key = CONFIG.PASS['consumer_key']
    consumer_secret = CONFIG.PASS['consumer_secret']
    access_token = CONFIG.PASS['access_token']
    access_secret = CONFIG.PASS['access_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # set up twitter api OAut token
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    print api
    wieght = wieght.encode('utf-8')
    wieght = int(wieght)
    max_tweets = 1000   # eliminate the number of tweets to control the rate limit.
    searched_tweets = [status for status in tweepy.Cursor(api.search,q=q,
                                          since= dateFrom ,until= dateTo,
                                           geocode= city).items(max_tweets)]

    tweets_data = []
    for line in searched_tweets:
        atweet = [str(line.user.screen_name.encode('utf-8')),
                     str(line.created_at),
                      str(line.text.encode('utf-8'))]

        words = line.text.encode('utf-8') #extracting only text for analysis
        words = cleanTweet(words)
        count = 0
        for w in words:
            if w in CDictionary.crimeDict:
                count += 1
        scale = count + wieght
        atweet.insert(0,scale)
        tweets_data.append(atweet)    # encoding text data

    return tweets_data
