from flask import Flask
from flask import request

from flask import render_template

app = Flask(__name__)
#url_for('static', filename='bootstrap.css')

@app.route('/')
def hello_world():
    return 'Hello Jacob Wolniewicz == Rapid Prototyping 2014!'

@app.route('/notify')
def notify():
    return 'notify that this is not built'

@app.route('/resume')
def resume():
	return 'no resume here!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']:
            return 'test'
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    temp = request.args.get('course', '')
    if temp == 'CSCI1300':
	    return 'Find class room for CSCI 1300... Atlas 100'
    if temp == 'CSCI2240':
	    return 'Find class room for CSCI 2240... ITLL 1B40'
    else:
	    return 'Find class room for CSCI 9999... No class room for CSCI 9999'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()