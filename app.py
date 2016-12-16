from flask import Flask , render_template 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('main.html')

@app.route('/<username>')
def swag(username):
	return 'Hello %s swagwefwef' % username

if __name__ == "__main__":
	app.run(debug=True)
