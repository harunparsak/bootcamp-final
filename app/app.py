from flask import Flask,render_template_string,request
from datetime import datetime
import psycopg2
import os
app=Flask(__name__)
conn=None
cur=None
if not os.environ.get("FLASK_TEST"):
    conn = psycopg2.connect(
        host="db",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            name TEXT,
            message TEXT
        );
    """)
    conn.commit()
html="""
<!doctype html>
<title>Mesaj Uygulaması</title>
<h1>Mesaj Gönder</h1>
<form method=post>
    İsim:<input type=text name=name><br>
    Mesaj:<input type=text name=message><br>
    <input type=submit value =Gönder>
</form>
<h2>Mesajlar</h2>
<ul>
    {% for msg in messages %}
        <li><b>{{ msg[0] }}</b>: {{ msg[1] }}</li>
    {%endfor%}
</ul>
"""
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        log_line = f"[{datetime.now()}] {name}: {message}\n"
        with open("logs/app.log", "a") as log_file:
            log_file.write(log_line)
        if cur:
            cur.execute("INSERT INTO messages(name, message) VALUES (%s, %s)", (name, message))
            conn.commit()
    if cur:
        cur.execute("SELECT name, message FROM messages ORDER BY id DESC")
        all_messages = cur.fetchall()
    else:
        all_messages = []
    return render_template_string(html, messages=all_messages)


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")

