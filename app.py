from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="postgres",
        password="1qaz1WSX@#",
        host="localhost",
        port="5432"
    )
    return conn

# Route to display the form
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

# Route to handle form submission
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
    conn.commit()
    cur.close()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
