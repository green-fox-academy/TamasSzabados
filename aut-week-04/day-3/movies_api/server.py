from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/movies', methods=['GET'])
def all_movies():
    return jsonify()


 @app.route('/api/movies/<movie_id>', methods=['GET'])
 def movie(movie_id):
    return jsonify()
    

    

if __name__ == '__main__':
    app.run(debug=True)