from flask import Flask, redirect, render_template, request
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconn import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friends')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM friends;"))

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html')

app.run(debug=True)