from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

firebaseConfig = {
    
    "apiKey": "AIzaSyAio8KVCa2S3ZvWk4FtRWEulsuYBTZIYHc",
    "authDomain": "aya2-dda25.firebaseapp.com",
    "databaseURL": "https://aya2-dda25-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "aya2-dda25",
    "storageBucket": "aya2-dda25.appspot.com",
    "messagingSenderId": "518108355111",
    "appId": "1:518108355111:web:7a96011a1a697f89278c02"
   
 };

    


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('main'))
        except:
            error = "Authentication failed"
            return render_template('signin.html', error=error)
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['mail']
        password = request.form['pass']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            user_id = user['localId']
            db.child("users").child(user_id).set({"name": name, "email": email})
            return redirect(url_for('main'))
        except Exception as e:
            error = "Authentication failed"
            return render_template('signup.html', error=error)
    return render_template('signup.html')

@app.route('/signout')
def signout():
    session.pop('user', None)
    auth.current_user = None
    return redirect(url_for('home'))

@app.route('/main', methods=['GET', 'POST'])
def main():
    if 'user' not in session:
        return redirect(url_for('signin'))

    view = 'main'
    message = None
    place = None
    reviews = []
    if request.method == 'POST':
    	print(request.form.keys())
    	if 'place' in request.form:
    		place = request.form['place']
    		view = 'experience'
    	if 'experience' in request.form:
    		place = request.form['place']
    		experience = request.form['experience']
    		user_id = session['user']['localId']
    		db.child("reviews").child(place).push({"user_id": user_id, "experience": experience})
    		message = "Thank you for your submission!"
    		view = 'main'
    	if 'see_reviews' in request.form:
    		print('jjj')
    		place = request.form['place']
    		reviews = db.child("reviews").child(place).get().val()
    		if reviews:
	        	reviews = [{"experience": rev["experience"], "user_id": rev["user_id"]} for rev in reviews.values()]
	    	view = 'reviews'

    return render_template('main.html', view=view, message=message, place=place, reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True, port=5003)