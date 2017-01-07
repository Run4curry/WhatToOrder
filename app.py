from flask import Flask , render_template , jsonify , request, url_for , redirect
from what2Order import what2Order




app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def mainpage():
	if request.method == "POST":
		restaurant = request.form['rest']
		address = request.form['address']
		returnFoodList , returnCountList = what2Order(restaurant,address)

		return render_template('main.html',returnFoodList=returnFoodList,returnCountList=returnCountList)

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
