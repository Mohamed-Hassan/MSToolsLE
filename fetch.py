
import twitter

CONSUMER_KEY = '7lO82bYVdJC9BTyqOGUnrXh5M'
CONSUMER_SECRET = 'TN2eCN33TRaKGSZRtXGBL5xccGljLzx6h2wiAnFVs4hQhP1DZG'
OAUTH_TOKEN = '809545887399706624-m6Fp4Vw8Xkezm0d88yyr13qfJAtpoKj'
OAUTH_TOKEN_SECRET = 'UnumW6OLy1FIa2wXs4hU8c3qUfTbsrwoYLvsrzymxk6WS'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

print twitter_api

q = "erie"
search_results = twitter_api.search.tweets(q=q)
print search_results
statuses = search_results['statuses']
print status_texts
status_texts = [ status['text']
                   for status in statuses ]
screen_names = [ user_mention['screen_name']
                  for status in statuses
                         for user_mention in status['entities']['user_mentions'] ]
hashtags = [ hashtag['text']
             for status in statuses
                for hashtag in status['entities']['hashtags'] ]