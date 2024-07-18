from flask import Flask,render_template 


app = Flask(__name__)

import random 

fortunes=["You will soon embark on a journey that will change your life.",
"A surprise gift will bring you great joy.",
"An unexpected opportunity will present itself soon.",
"Good fortune will smile upon you today.",
"A new friendship will blossom in the coming weeks.",
"You will achieve your goals through perseverance and hard work.",
"A pleasant surprise is in store for you this weekend.",
"You will find success in an unexpected place.",
"Your positive attitude will lead you to happiness.",
"A new adventure is on the horizon. Embrace it!"]



@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/fortune')
def fortune():
	random_fortune = random.choice(fortunes)
	print(random_fortune)



	
	return render_template("fortune.html",l_fortunes=random_fortune)



if __name__ == '__main__':
    app.run(debug=True)
