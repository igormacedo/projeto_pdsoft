 # -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import date
import sys
import cgi

app = Flask(__name__)

#MySQL configuration variables
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'include'
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
mysql = MySQL(app)

#Upload configuration variables
app.config['PICTURES_FOLDER'] = 'static/users/pictures'
app.config['ALLOWED_EXTENSIONS'] = set(['png','jpg'])

@app.route("/", methods=["GET","POST"])
def hello():

    cadastro = 0 # 0 - sem cadastro / 1 - cadastro com sucesso/ 2 - cadastro falhou

    if request.method == "POST":
        print("post request")
        cur = mysql.connection.cursor()
        login = request.form["cd_login"]
        senha = request.form["cd_senha"]
        email = request.form["cd_email"]
        nome = request.form["cd_nome"]
        mat = request.form["cd_matricula"]
        curso = request.form["cd_curso"]
        #foto = request.form['cd_pic']
        rua = request.form["cd_rua"]
        numero = request.form["cd_numero"]
        bairro = request.form["cd_bairro"]
        cidade = request.form["cd_cidade"]
        uf = request.form["cd_uf"]
        cep = request.form["cd_cep"]
        nascimento = request.form["cd_nascimento"]

        data = (login, senha, email, mat, nome, curso, rua, numero, bairro, cidade, uf, cep, date(1994, 5, 25))
        print(data)

        if validateData(login,senha,nome,mat,email):
            cur.execute("INSERT INTO members (login,senha,email,uniid,name,course,street,housenumber,neighborhood,city,state,cep,birth)"
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",data)
            row = cur.fetchall()
            mysql.connection.commit()
            cadastro = 1
        else:
            cadastro = 2

    return render_template("home.html", cadastro=cadastro)

def validateData(login,senha,nome,mat, email):
    if login == "":
        return False
    elif senha == "":
        return False
    elif nome == "":
        return False
    elif mat == "" or not(mat.isdigit()):
        return False
    elif email =="":
        return False
    return True

@app.route('/membersview')
def membersview():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM members")
    row = cur.fetchall()

    members = []
    for r in row:
        members.append(dict((cur.description[idx][0], value) for idx, value in enumerate(r)))

    print members
    return render_template("membersview.html", members = members)

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host="0.0.0.0")
