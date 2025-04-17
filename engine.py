import random

def analyze_packet(summary):
    suspicious_keywords = ['ftp', 'telnet', 'nmap', 'malformed']
    for keyword in suspicious_keywords:
        if keyword in summary.lower():
            return "Intrusion"
    return "Normal" if random.random() > 0.1 else "Intrusion"
