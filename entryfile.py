from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'BucketList'
mysql = MySQL(app)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route('/db')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM tbl_user''')
    rv = cur.fetchall()
    return str(rv)

@app.route("/my")
def other_hello():
    return "Other Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
