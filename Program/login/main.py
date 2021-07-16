from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = "1234353234"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "project"

db = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
        info = cursor.fetchone()
        if info is not None:
            if info['username'] == username and info['password'] == password:
                session['loginsuccess'] = True
                return redirect(url_for('profile'))
        else:
            return redirect(url_for('index'))

    return render_template("login2.html")


@app.route('/new/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template("profile.html")



if __name__ == "__main__":
    app.run(debug=True)
