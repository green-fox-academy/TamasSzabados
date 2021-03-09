from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    filename = f"movie{movie_id}.txt"
    with open(filename, 'r') as f:
        line = f.readlines()
        header = ""
        paragraph = ""
        for i,v in enumerate(line):
            if i == 0:
                header += v.strip()
            else:
                paragraph += v.strip()

    return render_template('movie.html', header = header, paragraph = paragraph)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)