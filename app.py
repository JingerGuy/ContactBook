from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.secret_key = "Secret Key"



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100))
 
    def __init__(self, name, phone, email):
 
        self.name = name
        self.phone = phone
        self.email = email

@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", contacts = all_data)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        my_data = Data(name, phone, email)
        db.session.add(my_data)
        db.session.commit()

        flash("Contact Inserted Successfully")

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():

        if request.method == 'POST':
            my_data = Data.query.get(request.form.get('id'))

            my_data.name = request.form['name']
            my_data.phone = request.form['phone']
            my_data.email = request.form['email']

            db.session.commit()
            flash("Contact Updated Successfully")


            return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Contact Deleted Successfully")
 
    return redirect(url_for('Index'))
 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
