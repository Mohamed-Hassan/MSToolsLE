from flask import Flask, render_template, request, json
from flask import redirect
from fechTweepy import fetch_tweets
from datetime import datetime


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
        city = "40.440625,-79.995886,25Km"
    elif request.form['city'] == 'Philadelphia':
        city = "39.9703447,-75.1377113,20km"
    elif request.form['city'] == 'Harrisburg':
        city = "40.273191,-76.886701,20km"

    dfrom = request.form['dfrom']
    dto = request.form['dTo']
    dfromobj = datetime.strptime(dfrom, '%m/%d/%Y') # to convert date format to date object
    dtoobj = datetime.strptime(dto, '%m/%d/%Y')
    dfrom = datetime.strftime(dfromobj, '%Y-%m-%d') # convert date from 01/01/2017 to 2017-01-01
    dto = datetime.strftime(dtoobj, '%Y-%m-%d')


    if len(request.form) == 5 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom= dfrom , dateTo= dto, city= city) # call fetch_tweets method and pass the form input
        alltweets = tweets
    elif len(request.form) == 7 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city)
        alltweets = tweets + tweets2
    elif len(request.form) == 9 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        alltweets = tweets + tweets2 + tweets3
    elif len(request.form) == 11 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city)
        alltweets = tweets + tweets2 + tweets3 + tweets4
    elif len(request.form) == 13 :
        wieght1 = request.form['wieght1']
        Keyword1 = request.form['Keyword1']
        tweets = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        wieght2 = request.form['wieght2']
        Keyword2 = request.form['Keyword2']
        tweets2 = fetch_tweets(q=Keyword2, dateFrom=dfrom, dateTo=dto, city= city)
        wieght3 = request.form['wieght3']
        Keyword3 = request.form['Keyword3']
        tweets3 = fetch_tweets(q=Keyword1, dateFrom=dfrom, dateTo=dto, city= city)
        wieght4 = request.form['wieght4']
        Keyword4 = request.form['Keyword4']
        tweets4 = fetch_tweets(q=Keyword4, dateFrom=dfrom, dateTo=dto, city= city)
        wieght5 = request.form['wieght5']
        Keyword5 = request.form['Keyword5']
        tweets5 = fetch_tweets(q=Keyword5, dateFrom=dfrom, dateTo=dto, city= city)
        alltweets = tweets + tweets2 + tweets3 + tweets4 + tweets5


    print  alltweets
    fd = request.form

    return render_template("UI.html", Response = alltweets, formData = fd )  # render the list tweet to UI.html





if __name__ == '__main__':
    app.run()
