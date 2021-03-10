from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route("/form")
def form():
    return render_template('form.html')

@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        default_name = '0'
        searchword  = request.form.get('name', default_name)

    with open("product.csv", "r") as f:
        lines = f.readlines()
        result = []
        for line in lines:
            word = line.split(";")
            if searchword in word[1]:
                result.append(line)
    return str(result)
    

if __name__ == '__main__':
    app.run(debug=True)