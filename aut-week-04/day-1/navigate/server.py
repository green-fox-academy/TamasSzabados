from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie1')
def movie1():
    return render_template('movie1.html')

@app.route('/movie2')
def movie2():
    return render_template('movie2.html')

@app.route('/movie3')
def movie3():
    return render_template('movie3.html')

@app.route('/movie4')
def movie4():
    return render_template('movie4.html')

@app.route('/movie5')
def movie5():
    return render_template('movie5.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)