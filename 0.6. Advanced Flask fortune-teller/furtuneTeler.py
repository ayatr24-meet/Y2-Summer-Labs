from flask import Flask,render_template 
import random
app = Flask(__name__)


	fortunes_list=["A thrilling adventure awaits you in the near future","Unexpected wealth will soon find its way to you.","A new friendship will bring joy and excitement into your life.",
"You will overcome a great challenge and emerge victorious.",
"A secret from your past will be revealed, changing your perspective.",
"An opportunity for growth and learning is on the horizon.",
"You will find love where you least expect it.",
"Your hard work will soon pay off in a significant way.",
"A journey you embark on will lead to self-discovery.",
"Trust your intuition; it will guide you to success."]

 
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/fortune')
def fortune():
	random_fortune=random.choice(fortunes)
	return render_template('fortune.html')




if __name__ == '__main__':
    app.run(debug=True)
