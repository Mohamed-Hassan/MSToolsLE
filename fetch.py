
import twitter

CONSUMER_KEY = '7lO82bYVdJC9BTyqOGUnrXh5M'
CONSUMER_SECRET = 'TN2eCN33TRaKGSZRtXGBL5xccGljLzx6h2wiAnFVs4hQhP1DZG'
OAUTH_TOKEN = '809545887399706624-m6Fp4Vw8Xkezm0d88yyr13qfJAtpoKj'
OAUTH_TOKEN_SECRET = 'UnumW6OLy1FIa2wXs4hU8c3qUfTbsrwoYLvsrzymxk6WS'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

print twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
print world_trends
print
print us_trends


