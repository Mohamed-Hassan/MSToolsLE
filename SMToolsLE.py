from flask import Flask, render_template, request, json
from flask import redirect



app = Flask(__name__)


@app.route('/')
def main():
    return render_template('UI.html')


@app.route('/Response', methods= ['POST', 'GET'])
def Response():
    # _dfrom = request.form['dfrom']
    # _dto = request.form['dTo']
    #return json.dump({'html':'<span> get received </span>'})
    # _dfrom,_dto
    dfrom = request.form['dfrom']
    dto = request.form['dTo']
    wight = request.form['wight']
    keyword = request.form['keyword']
    print dfrom
    print  dto
    print  wight
    print  keyword
    print request.form
    nse = request.form

    import tweepy
    from tweepy import OAuthHandler

    consumer_key = '7lO82bYVdJC9BTyqOGUnrXh5M'
    consumer_secret = 'TN2eCN33TRaKGSZRtXGBL5xccGljLzx6h2wiAnFVs4hQhP1DZG'
    access_token = '809545887399706624-m6Fp4Vw8Xkezm0d88yyr13qfJAtpoKj'
    access_secret = 'UnumW6OLy1FIa2wXs4hU8c3qUfTbsrwoYLvsrzymxk6WS'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    # print api

    query = keyword
    print query
    max_tweets = 50
    searched_tweets = [status.text.encode('utf-8') for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    print  searched_tweets



    return render_template("Response.html", Response = nse )





if __name__ == '__main__':
    app.run()
