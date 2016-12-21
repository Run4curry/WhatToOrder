from flask import Flask , render_template 
from bs4 import BeautifulSoup 
from urllib2 import urlopen
import json 

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('main.html')

@app.route('/<username>')
def swag(username):
	return 'Hello %s swagwefwef' % username

if __name__ == "__main__":
	app.run(debug=True)
