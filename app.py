from flask import Flask, request, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():

    # Prendo i dati inseriti in input dal form
    nome = request.form['firstName'].strip()
    cognome = request.form['lastName'].strip()
    email = request.form['email'].strip()

    if nome and cognome and email:
        print('variabili NON vuote')
        

    # print(nome, cognome, email) #stampo i dati inseriti per verifica

    # Ritorno alla pagina iniziale dopo aver inserito i dati
    return render_template('index.html')