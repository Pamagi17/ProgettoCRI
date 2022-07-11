from crypt import methods
from flask import Flask, redirect, request, render_template, url_for
import API.sendEmail as sendEmail

app = Flask (__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
url = '127.0.0.1:5000'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        firstName = request.form['firstName'].strip()
        lastName = request.form['lastName'].strip()
        email = request.form['email'].strip()

        if firstName and lastName and email:
            if sendEmail.sendEmail(email, firstName):
                return redirect(url_for('emailSent'))
            else:
                print('Unable to sendEmail')
        else:
            print('Data are not enriched')

    else: # GET request
        return render_template('form.html')

@app.route('/emailSent')
def emailSent():
    return render_template('emailSent.html')

if __name__ == "__main__":
    app.run(debug=True)