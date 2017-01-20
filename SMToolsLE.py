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
    Response = request.form
    return render_template("Response.html", Response=Response)





if __name__ == '__main__':
    app.run()
