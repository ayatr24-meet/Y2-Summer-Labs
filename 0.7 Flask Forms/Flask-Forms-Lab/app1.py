from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        birth_month = request.form.get('birth_month', '')
        if not birth_month:
            return "Error: Birth month not provided", 400
        return redirect(url_for('fortune', month=birth_month))
    return render_template('home1.html')

@app.route('/fortune')
def fortune():
    month = request.args.get('month', '')
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
    
   
    month_length = len(month)
    index = month_length % len(fortunes)
    
    
    fortune = fortunes[index]
    
   
    return render_template('fortune1.html', fortune=fortune)

if __name__ == '__main__':
    app.run(debug=True)