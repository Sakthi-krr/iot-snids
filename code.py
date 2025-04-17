from flask import Flask, render_template
import sqlite3
import threading
from packet_sniffer import start_sniffing

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

# Background packet sniffer
threading.Thread(target=start_sniffing, daemon=True).start()

@app.route('/')
def dashboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 50")
    logs = c.fetchall()
    conn.close()
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)