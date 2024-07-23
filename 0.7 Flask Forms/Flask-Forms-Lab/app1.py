from flask import Flask, render_template, request, redirect, url_for
from flask import session 

app = Flask(__name__,template_folder='templates',static_folder='static')
app.config['SECRET_KEY'] = "123456"
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        n= request.form['name']
        b= request.form['month']
        session['name']=n 
        session['birthmonth']=b 
        return redirect(url_for('home'))
    return render_template('home.html')
    

@app.route('/fortune1',methods=['GET'])
def fortune():
    
    fortunes = [
        "You will soon embark on a journey that will change your life.",
        "A surprise gift will bring you great joy.",
        "An unexpected opportunity will present itself soon.",
        "Good fortune will smile upon you today.",
        "A new friendship will blossom in the coming weeks.",
        "You will achieve your goals through perseverance and hard work.",
        "A pleasant surprise is in store for you this weekend.",
        "You will find success in an unexpected place.",
        "Your positive attitude will lead you to happiness.",
        "A new adventure is on the horizon. Embrace it!"
    ]

    month = session.get('birthmonth','')
    x = len(month)
    if x > 10 or x == 0 :
        return redirect(url_for('login'))
    f = fortunes[x]
    return render_template("fortune1.html", f=f)    
   
    

if __name__ == '__main__':
    app.run(debug=True)