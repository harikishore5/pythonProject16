from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="hari123",
                port='5432'

            )
            cur = conn.cursor()

            query = "INSERT INTO custome_login (name, email, password) VALUES (%s, %s, %s)"
            cur.execute(query, (name, email, password))

            conn.commit()
            conn.close()

            return redirect(url_for('success'))

        except Exception as e:
            return f"Error: {e}"

    return render_template('register.html')

@app.route('/success')
def success():
    return 'Success: You have been registered.'

if __name__ == '__main__':
    app.run(debug=True)
