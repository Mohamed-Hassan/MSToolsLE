from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('UI.html')


@app.route('/', methods= ['POST', 'GET'])
def receiveData():
    _dfrom = request.form['dfrom']
    _dto = request.form['dTo']
    return json.dump({'html':'<span> get received </span>'})
    # _dfrom,_dto





if __name__ == '__main__':
    app.run()
