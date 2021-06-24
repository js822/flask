from flask import Flask, app, render_template, url_for,request
from werkzeug.utils import escape
import mysql.connector

app = Flask(__name__, template_folder='template', static_folder='static')

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root123",
   database="efeone"
)
mycursor = mydb.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/returnbook')
def returnbook():
    return render_template('returnbook.html')

@app.route('/adduser')
def adduser():
    return render_template('adduser.html')

@app.route('/create', methods=['POST'])
def insert():
   id = escape(request.form['id'])
   name = escape(request.form['name'])
   gender = escape(request.form['gender'])
   age = escape(request.form['age'])
   sql = """ INSERT INTO user(id, name, gender, age)
   VALUES(%s, %s, %s, %s)"""
   val = (id, name, gender, age, )
   mycursor.execute(sql, val)
   mydb.commit()
   return render_template('index.html')

@app.route('/bcreate', methods=['POST'])
def insertb():
   
   bname = escape(request.form['bname'])
   athname = escape(request.form['athname'])
   publisher = escape(request.form['publisher'])
   price = escape(request.form['price'])
   pages = escape(request.form['pages'])
   sql = """ INSERT INTO book(book_name, author_name, publisher, price, pages)  
   VALUES(%s, %s, %s, %s, %s)"""
   val = (bname, athname, publisher, price, pages )
   mycursor.execute(sql, val)
   mydb.commit()
   return render_template('index.html')  


@app.route('/issuebook')
def issuebook():
    return render_template('booksearch.html')

if __name__ == '__main__':
    app.run(debug=True)