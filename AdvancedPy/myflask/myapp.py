from flask import Flask
from flask import render_template

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/whereami')
def whereami():
        return 'Ghana!'

@app.route('/login')
def login():
        return render_template('login.html')
if __name__ == '__main__':
    app.run(port = 5000,debug = True,)



