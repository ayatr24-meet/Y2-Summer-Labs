from flask import Flask, render_template, request, redirect, url_for
from flask import session 
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyAKMDmLjU_0Wt7cf7aq85coxWkUJv7YPkw",
  "authDomain": "ayaproject-c3a36.firebaseapp.com",
  "projectId": "ayaproject-c3a36",
  "storageBucket": "ayaproject-c3a36.appspot.com",
  "messagingSenderId": "469206502128",
  "appId": "1:469206502128:web:2f19d273a36c45d3781035",
  "databaseURL":"https://ayaproject-c3a36-default-rtdb.europe-west1.firebasedatabase.app/"
}


app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()



app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/signin' , methods=['GET','POST'])
def signin():
	if request.method=='POST':
		email=request.form['mail']
		password=request.form['pass']
		return redirect(url_for('home')) 
	try:
		session["quotes"]=[]

	except:
		error = "Authentication failed"
		print(error)
		return render_template('signin.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method=='POST':
		name=request.form['name']
		email=request.form['mail']
		password=request.form['pass']
		info = {"name": name,"email": email, "password":password}
		try:
			user = auth.create_user_with_email_and_password(email, password)
			session['user'] = user
			user_id = user['localId']
			db.child("users").child(user_id).update(info)
			return redirect(url_for('home'))
		except:
			error = "Authentication failed"
	return render_template('signup.html') 


@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html')










if __name__ == '__main__':
    app.run(debug=True)