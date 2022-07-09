from flask import Flask, request, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/', methods=['POST'])
def my_form_post():

    #Prendo i dati inseriti in input dal form
    nome = request.form['nome']
    cognome = request.form['cognome'] 
    email = request.form['email']

    print(nome, cognome, email) #stampo i dati inseriti per verifica

    return render_template('index.html') #ritorno alla pagina iniziale dopo aver inserito i dati