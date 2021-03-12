from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = "tomi"

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user = request.form['name']
        passwd = request.form['passwd']
        email = request.form['email']
        with open("users.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line == user:
                    return redirect(url_for('login'))
                    break
        with open("users.txt", "a+") as nf:
            nf.writelines("\n" + user)
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        passwd = request.form['passwd']
        found = 0
        with open("users.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line)
                if line == user:
                    session["user"] = user
                    session["passwd"] = passwd
                    found = 1
        print(found)
        if found == 0:
            return redirect(url_for('signup'))
        else:
            return redirect(url_for('welcome'))
    else:
        if "user" in session:
            return redirect(url_for('welcome'))
        return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if "user" in session:
        username = session["user"]
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))
        

if __name__ == '__main__':
    app.run(debug=True)