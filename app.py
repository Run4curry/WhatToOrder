from flask import Flask , render_template , jsonify , request, url_for , redirect
from bs4 import BeautifulSoup 
from urllib2 import urlopen
import json 
from Menu import GetMenu
from Review import GetReviews
from Whatfoods import Foodlist 



app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello swag!'

@app.route('/user/<username>', methods=["GET","POST"])
def swag(username):

	if request.method == "GET":
		people = []
	if request.method == "POST":
		people = ['Shiva','Aaron','Justin']

	return render_template('main.html',name=username,people=people)



if __name__ == "__main__":
	app.run(debug=True)
