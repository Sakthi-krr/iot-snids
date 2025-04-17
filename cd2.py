from scapy.all import sniff
from ids_engine import analyze_packet
import sqlite3

def log_to_db(packet_summary, status):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        summary TEXT,
        status TEXT
    )''')
    c.execute("INSERT INTO logs (summary, status) VALUES (?, ?)", (packet_summary, status))
    conn.commit()
    conn.close()

def process_packet(packet):
    summary = packet.summary()
    status = analyze_packet(summary)
    log_to_db(summary, status)
    print(f"[{status}] {summary}")

def start_sniffing():
    sniff(prn=process_packet, store=0)
