from flask import Flask, render_template, request, redirect, url_for
from flask import session 
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyAhRlfQVWTx76rOmZoF3cEOkx93d7CU-NU",
  "authDomain": "auth-lab-f2f44.firebaseapp.com",
  "projectId": "auth-lab-f2f44",
  "storageBucket": "auth-lab-f2f44.appspot.com",
  "messagingSenderId": "552607277799",
  "appId": "1:552607277799:web:ac4e667b8b6c9c0d1af842",
  "databaseURL":"https://auth-lab-f2f44-default-rtdb.europe-west1.firebasedatabase.app/"

} 





app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()




@app.route('/')
def main():
  full_name=request.form['full_name']
  email=request.form['email']
  username=request.form['username']
  if request.method=='POST' :

    return.render_template("signup.html")








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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  error=""
  if request.method == 'POST':
    email = request.form['mail']
    password = request.form['pass']
    user1= {'full_name':"" , 'email':"" , 'username':""}

    try:

      session['user']=auth.create_user_with_email_and_password(email, password)
      session['quotes'] = []
      uid=session['user']['localID']
      db.child('Users').child(uid).set(user1)
      return redirect(url_for('home'))
    except :
      error = "Authentication failed"
      print(error)
  return render_template('signup.html')




@app.route('/signout')
def signout():
    #session.pop('user')
    session['user']=None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('signin'))




@app.route ('/home' , methods=['GET', 'POST'])
def home():
  if request.method=='POST':
    new_quote=request.form['user quote']
    quote = {
      "text": quote_text
      "said_by": said_by
      "uid": uid 
    }
    db.child("quotes").push(quote)
    return redirect(url_for('thanks'))
  return render_template('home.html')


@app.route ('/display')
def display():
  return render_template('display.html')

@app.route('/thanks' , methods=['GET' , 'POST'])
def thanks():
  if request.method=='GET':
    return render_template('thanks.html')
  return render_template('thanks.html')

    

      



if __name__ == '__main__':
    app.run(debug=True)






