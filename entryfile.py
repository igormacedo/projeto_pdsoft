# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_mysqldb import MySQL
from datetime import date
from users import User

import sys
import os
import cgi

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

# MySQL configuration variables
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'include'
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
mysql = MySQL(app)

# Upload configuration variables
app.config['PICTURES_FOLDER'] = 'static/users/pictures'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg'])

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route("/", methods=["GET", "POST"])
def hello():
    if not current_user.is_anonymous:
        return render_template("home.html", pic=current_user.picture)
    else:
        return render_template("home.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    login = 0  # 0 - login / 1 - login com sucesso/ 2 - login invalido/ 3 - senha invalida
    cur = mysql.connection.cursor()
    if request.method == "POST":
        username = request.form["lg_username"]
        password = request.form["lg_password"]
        cur.execute("SELECT login, password, picture FROM members WHERE login = '{}';".format(username))
        tup = cur.fetchone()

        if not tup:
            login = 2
        else:
            if tup[1] != password:
                login = 3
            else:
                login = 1
                user = User(tup[0],tup[1],tup[2])
                login_user(user)
                return render_template("home.html", pic = current_user.picture)

    return render_template("login.html")

@login_manager.user_loader
def load_user(user_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT login, password, picture FROM members WHERE login = '{}';".format(user_id))
        tup = cur.fetchone()
        return User(tup[0], tup[1], tup[2])
    except mysql.connection.IntegrityError:
        return None

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("home.html")


def validateData(login, senha, nome, mat, email):
    if login == "":
        return False
    elif senha == "":
        return False
    elif nome == "":
        return False
    elif mat == "" or not(mat.isdigit()):
        return False
    elif email == "":
        return False
    return True


@app.route('/membersview')
@login_required
def membersview():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM members")
    row = cur.fetchall()

    members = []
    for r in row:
        members.append(
            dict((cur.description[idx][0], value) for idx, value in enumerate(r)))

    print members
    return render_template("membersview.html", members=members)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    cadastro = 0  # 0 - sem cadastro / 1 - cadastro com sucesso/ 2 - cadastro falhou
    cur = mysql.connection.cursor()
    cur.execute("SELECT login FROM members")
    row = cur.fetchall()

    logins = []
    for r in row:
        logins.append(r[0].encode("utf8"))

    if request.method == "POST":

        print("post request")
        login = request.form["cd_login"].encode('utf-8')
        senha = request.form["cd_senha"].encode('utf-8')
        email = request.form["cd_email"].encode('utf-8')
        nome = request.form["cd_nome"].encode('utf-8')
        mat = request.form["cd_matricula"].encode('utf-8')
        curso = request.form["cd_curso"].encode('utf-8')
        foto = request.form["cd_foto"].encode('utf-8')
        tel = request.form['cd_tel'].encode('utf-8')
        cel = request.form['cd_cel'].encode('utf-8')
        rua = request.form["cd_rua"].encode('utf-8')
        numero = request.form["cd_numero"].encode('utf-8')
        bairro = request.form["cd_bairro"].encode('utf-8')
        cidade = request.form["cd_cidade"].encode('utf-8')
        uf = request.form["cd_uf"].encode('utf-8')
        cep = request.form["cd_cep"].encode('utf-8')
        nascimento = request.form["cd_nascimento"].encode('utf-8')

        data = (mat, nome, curso, rua, numero, bairro, cidade, uf, cep,
                tel, cel, date(1994, 5, 25), email, foto, login, senha)
        print(data)

        if validateData(login, senha, nome, mat, email):
            try:
                cur.execute("INSERT INTO members (uniid,name,course,street,housenumber,neighborhood,city,state,cep,housephone,mobilephone,birth,email,picture,login,password)"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                row = cur.fetchall()
                mysql.connection.commit()
                cadastro = 1

                file = request.files['file']
                filename = file.filename
                print(filename)
                if file and allowed_file(file.filename):
                    print(os.path.join(
                        app.config['PICTURES_FOLDER'], filename))
                    file.save(os.path.join(
                        app.config['PICTURES_FOLDER'], filename))

            except mysql.connection.IntegrityError:
                cadastro = 3
            finally:
                cur.close()
        else:
            cadastro = 2

    return render_template("signup.html", cadastro=cadastro, logins=logins)

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host="0.0.0.0")
