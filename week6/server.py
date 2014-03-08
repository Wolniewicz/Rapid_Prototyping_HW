from flask import Flask
from flask import request
from flask import render_template
from flask import json
from collections import namedtuple as NT
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home (welcome=None, navigation=None):
	nt = NT( 'Navigation' , 'href  caption' ) 

	n1 = nt( 'http://python.org' , 'python' ) 
	n2 = nt( 'http://cython.org' , 'cython' ) 
	n3 = nt( 'http://jython.org' , 'jython' ) 
	n4 = nt( 'http://pypy.org/'  , 'pypy' ) 

	nav = ( n1 , n2 , n3 , n4 ) 
	return render_template('home.html', welcome="My Webpage", navigation=nav)

if __name__ == '__main__':
    app.run(debug=True)