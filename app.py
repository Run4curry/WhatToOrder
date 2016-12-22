from flask import Flask , render_template , jsonify , request, url_for , redirect
from bs4 import BeautifulSoup 
from urllib2 import urlopen
import json 
from Menu import GetMenu
from Review import GetReviews
from Whatfoods import Foodlist 



app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def mainpage():
	if request.method == "POST":
		restaurant = request.form['rest']
		address = request.form['address']
		return render_template('main.html',restaurant=restaurant,address=address)

	return render_template('main.html')

#@app.route('/user/<username>', methods=["GET","POST"])
#def swag(username):

#	if request.method == "GET":
#		people = []
#	if request.method == "POST":
#		people = ['Shiva','Aaron','Justin']
#	return render_template('main.html',name=username,people=people)



if __name__ == "__main__":
	app.run(debug=True)
