from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return('<html> <h1>Hii!</h1></html> <a href="/food"> <html>')

@app.route('/pets')
def pets():
    return('<html> <h1>Hii!</h1></html> <a href=\'/pets\'>See Pets!</a></html>')

@app.route('/space')
def space():
    return('<html> <h1>Hii!</h1></html> <a href=\'/space\'>See Space!</a></html>')

@app.route('/food1')
def food1():
    return ('<html><p>hi</p><html>')


if __name__ == '__main__':
    app.run(debug=True)