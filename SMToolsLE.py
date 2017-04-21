from flask import Flask, render_template, request
from fechTweepy import fetch_tweets
from datetime import datetime
from operator import itemgetter


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('UI.html')


@app.route('/Response', methods= ['POST', 'GET'])
def Response():
    # Erie        "42.129224,-80.085059,40km"
    # Pittsburgh    "40.440625, -79.995886,45Km"
    # Philadelphia   "39.9703447, -75.1377113,20km"
    # Harrisburg   "40.273191, -76.886701, 20km"
    if request.form['city'] == 'Erie':
        city = "42.129224,-80.085059,40km"
    elif request.form['city'] == 'Pittsburgh':
        city = "40.440625,-79.995886,35Km"
    elif request.form['city'] == 'Philadelphia':
        city = "39.9703447,-75.1377113,20km"
    elif request.form['city'] == 'Harrisburg':
        city = "40.273191,-76.886701,20km"
    elif request.form['city'] == 'Chicago':
        city = "41.8781,-87.6298,20km"
    elif request.form['city'] == 'all':
        city = " "

    dfrom = request.form['dfrom']
    dto = request.form['dTo']
    dfromobj = datetime.strptime(dfrom, '%m/%d/%Y') # to convert date format to date object
    dtoobj = datetime.strptime(dto, '%m/%d/%Y')
    dfrom = datetime.strftime(dfromobj, '%Y-%m-%d') # convert date from 01/01/2017 to 2017-01-01
    dto = datetime.strftime(dtoobj, '%Y-%m-%d')


    if len(request.form) == 5:
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom= dfrom , dateTo= dto, city= city, wieght= wieght1 ) # call fetch_tweets method and pass the form input
        alltweets = tweets
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 7 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        alltweets = tweets + tweets2
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 9 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword3, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        alltweets = tweets + tweets2 + tweets3
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 11 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword3, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        alltweets = tweets + tweets2 + tweets3 + tweets4
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 13 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword3, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 15 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword3, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 17 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword3, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        wieght6 = request.form['wieght6']
        Keyword6 = request.form['Keyword6']
        tweets6 = fetch_tweets(q=Keyword6, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght6)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5 + tweets6
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 19 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        wieght6 = request.form['wieght6']
        Keyword6 = request.form['Keyword6']
        tweets6 = fetch_tweets(q=Keyword6, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght6)
        wieght7 = request.form['wieght7']
        Keyword7 = request.form['Keyword7']
        tweets7 = fetch_tweets(q=Keyword7, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght7)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5 + tweets6 + tweets7
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 21 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        wieght6 = request.form['wieght6']
        Keyword6 = request.form['Keyword6']
        tweets6 = fetch_tweets(q=Keyword6, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght6)
        wieght7 = request.form['wieght7']
        Keyword7 = request.form['Keyword7']
        tweets7 = fetch_tweets(q=Keyword7, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght7)
        wieght8 = request.form['wieght8']
        Keyword8 = request.form['Keyword8']
        tweets8 = fetch_tweets(q=Keyword8, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght8)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5 + tweets6 + tweets7 + tweets8
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 23 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        wieght6 = request.form['wieght6']
        Keyword6 = request.form['Keyword6']
        tweets6 = fetch_tweets(q=Keyword6, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght6)
        wieght7 = request.form['wieght7']
        Keyword7 = request.form['Keyword7']
        tweets7 = fetch_tweets(q=Keyword7, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght7)
        wieght8 = request.form['wieght8']
        Keyword8 = request.form['Keyword8']
        tweets8 = fetch_tweets(q=Keyword8, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght8)
        wieght9 = request.form['wieght9']
        Keyword9 = request.form['Keyword9']
        tweets9 = fetch_tweets(q=Keyword9, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght9)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5 + tweets6 + tweets7 + tweets8 + tweets9
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)
    elif len(request.form) == 25 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght1)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght2)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght3)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght4)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city, wieght= wieght5)
        wieght6 = request.form['wieght6']
        Keyword6 = request.form['Keyword6']
        tweets6 = fetch_tweets(q=Keyword6, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght6)
        wieght7 = request.form['wieght7']
        Keyword7 = request.form['Keyword7']
        tweets7 = fetch_tweets(q=Keyword7, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght7)
        wieght8 = request.form['wieght8']
        Keyword8 = request.form['Keyword8']
        tweets8 = fetch_tweets(q=Keyword8, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght8)
        wieght9 = request.form['wieght9']
        Keyword9 = request.form['Keyword9']
        tweets9 = fetch_tweets(q=Keyword9, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght9)
        wieght10 = request.form['wieght10']
        Keyword10 = request.form['Keyword10']
        tweets10 = fetch_tweets(q=Keyword10, dateFrom=dfrom, dateTo=dto, city=city, wieght=wieght10)

        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5 + tweets6 + tweets7 + tweets8 + tweets9 + tweets10
        soredTweets = sorted(alltweets, key=itemgetter(0), reverse=True)



    #print  alltweets
    fd = request.form.to_dict()

    return render_template("UI.html", Response = soredTweets, formData = fd )  # render the list tweet to UI.html





if __name__ == '__main__':
    app.run()
