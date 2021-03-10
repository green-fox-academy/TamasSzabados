from flask import Flask, request, render_template

app = Flask(__name__)

username = ""
password = ""

@app.route('/signup')
def signup():
    pass

@app.route('/login')
def login():
    pass


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', username=username)
        

if __name__ == '__main__':
    app.run(debug=True)