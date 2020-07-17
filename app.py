from flask import Flask, render_template,request
from database.db import Database
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        request_mail = request.form['email']
        if not Database.emailExists(request_mail):
            Database.insertEmailInDB(request_mail)
            return render_template('index.html', message='success')
        else:
            return render_template('index.html', message='failed')
    return render_template('index.html', message='')


if __name__ == '__main__':
    Database.createDb()
    app.run(debug=True)