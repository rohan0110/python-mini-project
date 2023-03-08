from flask import Flask, render_template, request, redirect,url_for,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user_info'
mysql = MySQL(app)



@app.route('/')
def hello_world():  # put application's code here
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        # Create a new cursor and execute the query
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, username, password) VALUES (%s, %s, %s, %s)", (name, email, username, password))
        
        # Commit changes to the database and close the cursor
        mysql.connection.commit()
        cur.close()
        
        # Redirect to the login page
        return redirect('/login')
    
    # Render the registration form template
    return render_template('register.html')


@app.route('/index')
def index():
    return render_template('index.php')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run()
