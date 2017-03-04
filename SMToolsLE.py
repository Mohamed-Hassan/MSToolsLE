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
    # _dfrom = request.form['dfrom']
    # _dto = request.form['dTo']
    #return json.dump({'html':'<span> get received </span>'})
    # _dfrom,_dto
    dfrom = request.form['dfrom']
    dto = request.form['dTo']
    wight = request.form['wight']
    keyword = request.form['keyword']
    dfromobj = datetime.strptime(dfrom, '%m/%d/%Y') # to convert date format to date object
    dtoobj = datetime.strptime(dto, '%m/%d/%Y')
    dfrom = datetime.strftime(dfromobj, '%Y-%m-%d') # convert date from 01/01/2017 to 2017-01-01
    dto = datetime.strftime(dtoobj, '%Y-%m-%d')
    print dfrom  # just for testing
    print  dto
    print  wight
    print  keyword
    print request.form
    nse = request.form
    tweets = fetch_tweets(q=keyword, dateFrom= dfrom , dateTo= dto) # call fetch_tweets method and pass the form input

    print  tweets

    return render_template("UI.html", Response = tweets )  # render the list tweet to UI.html





if __name__ == '__main__':
    app.run()
