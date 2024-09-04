from flask import Flask, render_template, request, redirect,url_for
import mysql.connector 

app = Flask(__name__)


db_config = {
    'host':'db', 
    'user':'root',
    'password':'joaomysql',
    

}
conn=mysql.connector.connect(**db_config)

@app.route("/")
def index():
    

    return render_template('index.html')

@app.route("/envio", methods=["POST"])
def envio():
        if request.method=="POST":
         email = request.form ["email"]
         mensagem = request.form ["mensagem"]
         #conn = mysql.connector.connect(**db_config)
         cursor = conn.cursor()
         cursor.execute('use sorteio;')
         cursor.execute('INSERT INTO sorteio(email, texto) VALUES (%s, %s)',(email, mensagem))
         conn.commit()
         cursor.close()
         return redirect(url_for ("sorteio"))

@app.route("/contatos.html")
def contatos():
    return render_template("contatos.html")

@app.route("/sobreogame.html")
def sobreogame():
    return render_template("sobreogame.html")

@app.route("/sorteio.html")
def sorteio():
    return render_template("sorteio.html")

@app.route("/index.html")
def inicio():
    return render_template("index.html")


app.run(debug=True)
