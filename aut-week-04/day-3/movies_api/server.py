from flask import Flask, request, jsonify, render_template, url_for
import json

app = Flask(__name__)

with open('movies.json') as f:
  data = json.load(f)

@app.route('/')
def index():
    return "<h3> This is my first movie api</h3>"

@app.route('/api/movies', methods=['GET', 'POST'])
def all_movies():
    if request.method == 'GET':
        return jsonify(data)
    elif request.method == 'POST':
        api_key = request.args["API_KEY"]
        if api_key == "hello":
            new_dict = {}
            new_dict["id"] = request.args['id']
            new_dict["title"] = request.args['title']
            new_dict["year"] = request.args['year']
            new_dict["genre"] = request.args['genre']
            new_dict["description"] = request.args['description']
            data.append(new_dict)
            with open('movies.json', 'w') as json_file:
                json.dump(data, json_file)
            return jsonify([new_dict]), 200
        else:
            return jasonify(["inncorrect api key"]),403
    
@app.route('/api/movies/<movie_id>', methods=['GET','PUT', 'DELETE'])
def movie(movie_id):
    if request.method == 'GET':
        movie_select = []
        for i in data:
            print(i)
            if i['id'] == int(movie_id):
                movie_select.append(i)
        return jsonify(movie_select)

    elif request.method == "PUT":
        api_key = request.args["API_KEY"]
        if api_key == "hello":
            found = False
            for i in data:
                if i['id'] == int(movie_id):
                    found = True
                    i["title"] = request.args['title']
                    i["year"] = request.args['year']
                    i["genre"] = request.args['genre']
                    i["description"] = request.args['description']
                    with open('movies.json', 'w') as json_file:
                        json.dump(data, json_file)
                    return jsonify([i]), 200
            if not found:
                return jsonify([{"error": "No movie found with <movie_id> ID"}]),404
        else:
            return jsonify(["inncorrect api key"]),403

    elif request.method == "DELETE":
        api_key = request.args["API_KEY"]
        if api_key == "hello":
            found = False
            for i in data:
                if i['id'] == int(movie_id):
                    found = True
                    data.remove(i)
                    with open('movies.json', 'w') as json_file:
                        json.dump(data, json_file)
                    return jsonify(["deleted"]), 200
            if not found:
                return jsonify([{"error": "No movie found with <movie_id> ID"}]),404
        else:
            return jsonify(["inncorrect api key"]),403

@app.route('/movies', methods=['GET'])
def welcome():
    return render_template('index.html', data=data)

@app.route('/edit-movie/<movie_id>', methods=['GET','POST'])
def edit_movie(movie_id):
    if request.method == 'GET':
        return render_template('edit_form.html', movie_id=movie_id)
    else:
        pass

@app.route('/add-movie', methods=['GET','POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('create_form.html')
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)